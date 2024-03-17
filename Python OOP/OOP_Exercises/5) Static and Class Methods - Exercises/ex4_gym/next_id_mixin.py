class NextIdMixin:
    id = 0      # not necessary, we avoid warnings with it

    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def increment_id(cls):
        cls.id += 1