"""Documentation about the fairsharer module."""


def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.

    In each iteration the highest value in "values" gives a fraction (share)
    to both the left and right neighbor.
    The leftmost field is considered the neighbor of the rightmost field.

    Examples:
        fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Args:
        values: list of numbers
        num_iterations: number of iterations
        share: fraction given to EACH neighbor

    Returns:
        New redistributed list
    """

    # Copy values so we don't overwrite the original list
    values_new = [float(v) for v in values]
    n = len(values_new)

    # Repeat redistribution num_iterations times
    for _ in range(num_iterations):

        # 1. max_val and idx of greatest value
        max_val = max(values_new)
        idx = values_new.index(max_val)  # leftmost max if tie

        # 2. indices of neighbors (circular)
        left_idx = (idx - 1) % n
        right_idx = (idx + 1) % n

        # 3. compute transfer amount
        transfer = max_val * share

        # 4. add to neighbors
        values_new[left_idx] += transfer
        values_new[right_idx] += transfer

        # 5. reduce the max value itself
        values_new[idx] -= 2 * transfer

    return values_new

print(fair_sharer([0, 1000, 800, 0], 1))
print(fair_sharer([0, 1000, 800, 0], 2))