from cypher import normalize
from cypher import square
from cypher import pad
from cypher import encrypt
from cypher import encryptComplete


def test_normalize():
	assert normalize("Text that must be normalized!") == "textthatmustbenormalized"
	assert normalize("Texts that must be normalized!") == "textsthatmustbenormalized"
	assert normalize("Is this code going to work? Let's see!") == "isthiscodegoingtoworkletssee"

def test_square():
	assert square("textthatmustbenormalized") == ["textt","hatmu","stben","ormal","ized"]
	assert square("textsthatmustbenormalized") == ["texts","thatm","ustbe","norma","lized"]
	assert square("isthiscodegoingtoworkletssee") == ['isthis','codego','ingtow','orklet','ssee']

def test_pad():
	assert pad(["textt","hatmu","stben","ormal","ized"]) == ["textt","hatmu","stben","ormal","ized!"]
	assert pad(["texts","thatm","ustbe","norma","lized"]) == ["texts","thatm","ustbe","norma","lized"]
	assert pad(['isthis','codego','ingtow','orklet','ssee']) == ['isthis','codego','ingtow','orklet','ssee!!']

def test_encrypt():
	assert encrypt(["textt","hatmu","stben","ormal","ized!"]) == "thsoieatrzxtbmetmeadtunl!"
	assert encrypt(["texts","thatm","ustbe","norma","lized"]) == "ttunlehsoixatrzttbmesmead"
	assert encrypt(['isthis','codego','ingtow','orklet','ssee!!']) == "iciossonrstdgkehetleigoe!sowt!"

def test_encryptComplete():
	assert encryptComplete("Text that must be normalized!") == "thsoieatrzxtbmetmeadtunl"
	assert encryptComplete("Texts that must be normalized!") == "ttunlehsoixatrzttbmesmead"
	assert encryptComplete("Is this code going to work? Let's see!") == "iciossonrstdgkehetleigoesowt"