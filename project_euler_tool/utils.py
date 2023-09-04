from pathlib import Path


def cache_on_disk(func):
    """Cache the result of a function on disk."""

    def wrapper(*args, **kwargs):
        """Wrapper function."""
        force = kwargs.pop("force", False)
        cache_path = Path("cache") / func.__name__
        cache_path.mkdir(parents=True, exist_ok=True)
        cache_file = cache_path / f"{'_'.join(map(str, args))}.html"
        if not force and cache_file.exists():
            with open(cache_file, "r") as file:
                return file.read()
        result = func(*args, **kwargs)
        with open(cache_file, "w") as file:
            file.write(result)
        return result

    return wrapper
