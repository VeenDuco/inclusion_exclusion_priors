import numpy as np
from scipy.interpolate import interp1d
import asreviewcontrib.insights.plot
from asreviewcontrib.insights.utils import _iter_states
from asreviewcontrib.insights.utils import _pad_simulation_labels

def plot_average_recall(
    ax,
    state_file_paths,
    priors=False,
    show_ci=True,
    ci_alpha=0.2,
    show_random=True,
    show_optimal=True,
    legend_label="Mean Recall",
    line_color="blue",
    legend_kwargs=None,
):
    """
    Plot the average recall curve across multiple state files, overlaying individual lines.

    Parameters
    ----------
    ax : plt.axes.Axes
        The matplotlib axis to plot on.
    state_file_paths : list of str
        List of state file paths to compute individual recall curves.
    priors : bool, optional
        Include the prior labels, by default False.
    show_ci : bool, optional
        If True, display the confidence interval, by default True.
    ci_alpha : float, optional
        Transparency of the confidence interval, by default 0.2.
    show_random : bool, optional
        If True, add the random recall curve, by default True.
    show_optimal : bool, optional
        If True, add the optimal recall curve, by default True.
    legend_label : str, optional
        Label for the mean recall curve in the legend, by default "Mean Recall".
    line_color : str, optional
        Color for the mean recall curve, by default "blue".
    legend_kwargs : dict, optional
        Additional arguments for the legend, by default None.

    Returns
    -------
    plt.axes.Axes
    """
    common_x = np.linspace(0, 1, num=100)
    interpolated_recalls = []

    # Generate state objects and plot individual recall curves
    for state_obj in _iter_states(state_file_paths):
        labels = _pad_simulation_labels(state_obj, priors=priors)
        x, recall = _recall_values(labels)
        
        # Interpolate recall values at common x points
        interp_func = interp1d(x, recall, kind="linear", bounds_error=False, fill_value=(0, 1))
        interpolated_recalls.append(interp_func(common_x))

        # Plot individual recall curves in gray
        ax.plot(x, recall, color="gray", alpha=0.6, linewidth=0.8, label="_nolegend_")

    # Calculate the mean and confidence intervals for recall
    interpolated_recalls = np.array(interpolated_recalls)
    mean_recall = np.mean(interpolated_recalls, axis=0)

    # Plot the mean recall curve
    ax.plot(common_x, mean_recall, label=legend_label, color=line_color, linewidth=2)

    if show_ci:
        lower_recall = np.percentile(interpolated_recalls, 5, axis=0)
        upper_recall = np.percentile(interpolated_recalls, 95, axis=0)
        ax.fill_between(common_x, lower_recall, upper_recall, color=line_color, alpha=ci_alpha)

    # Add random recall curve
    if show_random:
        ax.plot(common_x, common_x, color="black", linestyle="--", label="Random Recall")

    # Add optimal recall curve
    if show_optimal:
        ax.plot([0, 1], [0, 1], color="green", linestyle="-.", label="Optimal Recall")

    # Add legend if necessary
    if legend_kwargs is None:
        ax.legend()
    else:
        ax.legend(**legend_kwargs)

    # Set axis labels and title
    ax.set_title("Average Recall Curve with Individual Curves")
    ax.set_xlabel("Proportion of Records Reviewed")
    ax.set_ylabel("Recall")
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])

    return ax


def _recall_values(labels):
    """
    Compute recall values.

    Parameters
    ----------
    labels : list
        List of labels indicating whether each record is relevant.

    Returns
    -------
    tuple
        x (proportion of records reviewed), recall (cumulative recall values).
    """
    n_total = len(labels)
    n_relevant = sum(labels)
    x = np.arange(1, n_total + 1) / n_total
    recall = np.cumsum(labels) / n_relevant
    return x, recall



def plot_average_recall_two_groups(
    ax,
    state_file_paths_group1,
    state_file_paths_group2,
    priors=False,
    show_ci=True,
    ci_alpha=0.2,
    show_random=True,
    show_optimal=True,
    legend_labels=("Mean Recall Group 1", "Mean Recall Group 2"),
    colors=("blue", "red"),
    legend_kwargs=None,
):
    """
    Plot the average recall curve for two groups of state files, overlaying individual lines.

    Parameters
    ----------
    ax : plt.axes.Axes
        The matplotlib axis to plot on.
    state_file_paths_group1 : list of str
        List of state file paths for the first group.
    state_file_paths_group2 : list of str
        List of state file paths for the second group.
    priors : bool, optional
        Include the prior labels, by default False.
    show_ci : bool, optional
        If True, display the confidence interval, by default True.
    ci_alpha : float, optional
        Transparency of the confidence interval, by default 0.2.
    show_random : bool, optional
        If True, add the random recall curve, by default True.
    show_optimal : bool, optional
        If True, add the optimal recall curve, by default True.
    legend_labels : tuple, optional
        Labels for the mean recall curves of the two groups, by default
        ("Mean Recall Group 1", "Mean Recall Group 2").
    colors : tuple, optional
        Colors for the mean recall curves of the two groups, by default ("blue", "red").
    legend_kwargs : dict, optional
        Additional arguments for the legend, by default None.

    Returns
    -------
    plt.axes.Axes
    """
    common_x = np.linspace(0, 1, num=100)  # Define common_x here for all plots

    def _plot_group(state_file_paths, mean_color, individual_color, legend_label):
        interpolated_recalls = []

        # Generate state objects and plot individual recall curves
        for state_obj in _iter_states(state_file_paths):
            labels = _pad_simulation_labels(state_obj, priors=priors)
            x, recall = _recall_values(labels)
            
            # Interpolate recall values at common x points
            interp_func = interp1d(x, recall, kind="linear", bounds_error=False, fill_value=(0, 1))
            interpolated_recalls.append(interp_func(common_x))

            # Plot individual recall curves
            ax.plot(x, recall, color=individual_color, alpha=0.4, linewidth=0.8, label="_nolegend_")

        # Calculate the mean and confidence intervals for recall
        interpolated_recalls = np.array(interpolated_recalls)
        mean_recall = np.mean(interpolated_recalls, axis=0)

        # Plot the mean recall curve
        ax.plot(common_x, mean_recall, label=legend_label, color=mean_color, linewidth=2)

        if show_ci:
            lower_recall = np.percentile(interpolated_recalls, 5, axis=0)
            upper_recall = np.percentile(interpolated_recalls, 95, axis=0)
            ax.fill_between(common_x, lower_recall, upper_recall, color=mean_color, alpha=ci_alpha)

    # Plot group 1
    _plot_group(state_file_paths_group1, colors[0], "lightskyblue", legend_labels[0])

    # Plot group 2
    _plot_group(state_file_paths_group2, colors[1], "lightsalmon", legend_labels[1])

    # Add random recall curve
    if show_random:
        ax.plot(common_x, common_x, color="black", linestyle="--", label="Random Recall")

    # Add optimal recall curve
    if show_optimal:
        ax.plot([0, 1], [0, 1], color="green", linestyle="-.", label="Optimal Recall")

    # Add legend if necessary
    if legend_kwargs is None:
        ax.legend()
    else:
        ax.legend(**legend_kwargs)

    # Set axis labels and title
    ax.set_title("Average Recall Curve for Two Groups")
    ax.set_xlabel("Proportion of Records Reviewed")
    ax.set_ylabel("Recall")
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])

    return ax
