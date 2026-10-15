class Repository[T]:
    """ Rpository holds the items in a dictionary of the models.
    """
    def __init__(self):
        self._items: dict[int, T] = {}

    def add(self, item: T) -> None:
        """
        Adds item to the the Repository.

        Parameters
        ----------
        item : T
            Item being added to the repository.

        Returns
        -------
        None


        """

        self._items[item.id] = item

    def get (self, item_id: int) -> T:
        """
        Returns the item based on the id we want.

        Parameters
        ----------
        item_id : int
            DESCRIPTION.

        Returns
        -------
        T
            Returns the item with the id.

        """
        return self._items[item_id]

    def generate_id(self) -> int:
        return len(self._items)
