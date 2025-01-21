import gdown

# URL của tệp Google Drive
url = "https://drive.google.com/uc?id=1j0EcdlTBbF7-zcQtjIVWUqVh4yNJ2d7B"

# Đường dẫn lưu tệp sau khi tải
output = "/home/hoangphuc/Paper2/PRIPOR/data/msmarco-full/doc2query/query_to_docid.train.json"  # Hoặc đổi tên tùy ý

# Tải tệp
gdown.download(url, output, quiet=False)

print("Tải tệp thành công!")
