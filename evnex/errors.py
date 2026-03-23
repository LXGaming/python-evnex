from evnex.models import EvnexRateLimit


class NotAuthorizedException(ValueError):
    pass


class RateLimitException(ValueError):
    rate_limit: EvnexRateLimit | None

    def __init__(self, rate_limit: EvnexRateLimit | None):
        self.rate_limit = rate_limit
