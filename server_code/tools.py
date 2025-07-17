import hashlib
import uuid
import time

def generate_hash_id(seed: str = None, length: int = 12) -> str:
  """
    Generate a unique hash string, optionally based on a seed value.
    
    Args:
        seed (str): Optional string to base the hash on.
        length (int): Length of the hash string to return.
    
    Returns:
        str: A shortened unique hash string.
    """
  if seed is None:
    seed = f"{uuid.uuid4()}-{time.time_ns()}"

  hash_obj = hashlib.sha256(seed.encode())
  return hash_obj.hexdigest()[:length]
  