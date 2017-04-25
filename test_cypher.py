from cypher import normalize
from cypher import square
from cypher import encrypt


def test_normalize():
	assert normalize("Text that must be normalized!") == "textthatmustbenormalized"

def test_square():
	assert square("textthatmustbenormalized") == ["textt","hatmu","stben","ormal","ized"]

def test_encrypt():
	assert encrypt(["textt","hatmu","stben","ormal","ized"]) == ["thsoi","eatrz","xtbme","tmead","tunl"]