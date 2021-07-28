import hashlib

# input data from this tx: https://etherscan.io/tx/0x2ffab53ad9ba51d756d125004baf990a6456f625a2183719aa8e46bee140ad67
# equivalent to the "raw" field from https://docs.bisontrails.co/docs/submitting-deposit-data
input_data = bytes.fromhex("22895118000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000e000000000000000000000000000000000000000000000000000000000000001204e52f60af2c4e25cecf7f6a3612e699f37f831c4268332646353983658defa150000000000000000000000000000000000000000000000000000000000000030b715d61f9c4f892d6351f91f942534a7ca8385d4bd7d63aa3ca6d78f83ef052b06c54c52b5ab35becee8b6992410522200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002000a03ec8e439a0a061a58c05cc786cc244f9527963304c10918c966cbc173b7f0000000000000000000000000000000000000000000000000000000000000060b240b41c0434262af2c2a17e4d8b9976c469c9b2781a14d9a6ddd9a73391ed0b77d72126696c89bf6434fd006aeb974f126437581307f64655cd92f5a05bc6d62612b0d66f4174da232d0de7b06e2e539f5cdc44d03e8e26b878389c6d1c11c2")
# remove selector
input_data = input_data[4:]

# split input data into 32 bytes chunks
input_chunks = [input_data[i:i+32] for i in range(0, len(input_data), 32)]

# nested hashing
input_data_hash = hashlib.sha256(input_chunks[0]).digest()

for chunk in input_chunks[1:]:
    tmp = input_data_hash + chunk
    input_data_hash = hashlib.sha256(tmp).digest()

print(f'hash to sign: {input_data_hash.hex()}')
# 934694e2e2b709386ff5b7b0ae32562ff35dc7369e43d1ecdde8f344c34c1e24