class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):  # Inherits from the abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of your child item!
        self.name = args[0]

    def component_function(self):
        # Print the name of your child item here!
        print("{}".format(self.name))


class Composite(Component):  # Inherits from the abstract class, Component
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of the composite object
        self.name = args[0]

        # This is where we keep our child items
        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):
        # Print the name of the composite object
        print("{}".format(self.name))

        # Iterate though the child objects and invoke their component function
        for i in self.children:
            i.component_function()


# Build a composite submenu 1
sub1 = Composite("---submenu 1")

# Create a new child sub_submenu 1.1
sub11 = Child("------sub_submenu 1.1")
# Create a new child sub_submenu 1.2
sub12 = Child("------sub_submenu 1.2")

# Add the sub_submenu 1.1 to submenu 1
sub1.append_child(sub11)
# Add the sub_submenu 1.2 to submenu 1
sub1.append_child(sub12)

# Build a top-level composite menu
top = Composite("-top_menu")

# Build a submenu 2 thst is not a composite
sub2 = Child("---submenu 2")

# Add the composite submenu 1 and 2 to the top-level composite menu
top.append_child(sub1)
top.append_child(sub2)

# Let's test if our Composite pattern works!
top.component_function()
