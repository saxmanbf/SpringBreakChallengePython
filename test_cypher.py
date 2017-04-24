from cypher import normalize

def test_answer():
	assert normalize("Text that must be normalized!") == "textthatmustbenormalized"