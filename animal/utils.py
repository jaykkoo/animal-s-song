
def get_subclass_name_list(base_model):
    return [(subclass.__name__, subclass.__name__) for subclass in base_model.__subclasses__()]
