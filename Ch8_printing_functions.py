# Collection of functions used for Exercises in file 'Ch8_Ex15.py'

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left. Move each design to 'complete_models' after printing."""
    while unprinted_designs:
        current_designs = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model:", current_designs)
        completed_models.append(current_designs)


def show_completed_models(completed_models):
    """Show all models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
