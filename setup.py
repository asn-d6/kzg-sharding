from typing import Optional

from py_ecc import optimized_bls12_381 as b
from py_ecc.fields import optimized_bls12_381_FQ as FQ, optimized_bls12_381_FQ2 as FQ2
from py_ecc.typing import Optimized_Point3D


MODULUS = b.curve_order

_setup = None  # type: Optional[([Optimized_Point3D[FQ]], [Optimized_Point3D[FQ2]])]


def generate_setup(s: int, size: int) -> None:
    global _setup
    """
    # Generate trusted setup, in coefficient form.
    # For data availability we always need to compute the polynomials anyway, so it makes little sense to do things in Lagrange space
    """
    _setup = (
        [b.multiply(b.G1, pow(s, i, MODULUS)) for i in range(size + 1)],
        [b.multiply(b.G2, pow(s, i, MODULUS)) for i in range(size + 1)],
    )


def get_setup() -> ([Optimized_Point3D[FQ]], [Optimized_Point3D[FQ2]]):
    assert _setup is not None
    return _setup
