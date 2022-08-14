# Phân loại văn bản tiếng Việt

Đề tài nghiên cứu về bài toán *phân loại văn bản tiếng Việt*, được nhóm sinh viên thực hiện trong quá trình học môn Xử lý ngôn ngữ tự nhiên Nâng cao - Khoá 31 trường Đại học Khoa học Tự nhiên, ĐHQG-HCM

**Nhóm Sinh viên tham gia đề tài** 

* Huỳnh Viết Thám ([21C11027@student.hcmus.edu.vn](21C11027@student.hcmus.edu.vn))
* Lê Công Luận ([21C11013@student.hcmus.edu.vn](21C11013@student.hcmus.edu.vn))
* Nguyễn Thành Thái ([21C11026@student.hcmus.edu.vn](21C11026@student.hcmus.edu.vn))


## Nội dung chính của Project này gồm 3 thư mục chính

* [classification](#classification)
* [phoBert](#phoBert)
* [Các file trên Colab](#Colab)

## classification

Thư mục có chứa model đã được huấn luyện sẵn trên 02 bộ dữ liệu Foody và VNTC.
Để chạy kiểm thử model, có thể chạy theo các lệnh sau:

- Đối với việc chạy phân loại thư mục
```
$ python classificationRoot.py --text "Nội dung cần phân loại"
```
- Đối với việc chạy phân loại phản hồi tích cực và tiêu cực
```
$ python classificationSVM2.py --text "Nội dung cần phân loại"
```

## phoBert

Thư mục chứa file train và các tài liệu liên quan khi nhóm thực hiện trên mô hình phoBert.

## Colab

Trong đây bao gồm 3 file Google Colab:
- phobert được thử chạy trên Colab
- transformers_bartpho
- Ví dụ về TF-IDF

## Kết quả thử nghiệm 

Kết quả các thử nghiệm kết hợp mô hình SVM và các đặc trưng Tfidf trên hai bộ dữ liệu VNTC và Foody.
- Trên bộ dữ liệu VNTC

| Mô hình                                         | F1 %     |Accuracy |
|-------------------------------------------------|----------|---------|
| TfidfVectorizer(ngram_range=(1, 2), max_df=0.8) | **92.37**|**92.37**|
| Mô hình kết hợp phoBert                         | 85.05    | 85.05   |

- Trên bộ dữ liệu Foody
| Mô hình                                         | F1 %     |Accuracy |
|-------------------------------------------------|----------|---------|
| TfidfVectorizer(ngram_range=(1, 2), max_df=0.8) | **87.41**|**87.41**|
| Mô hình kết hợp phoBert                         | 85.27    | 85.27   |


## Lời cảm ơn
Xin chân thành cảm ơn các nhóm phát triển sklearn, fasttext đã tạo ra những công cụ hữu ích để nhóm sử dụng trong các thử nghiệm của mình. Nhóm xin chân thành cảm ơn mã nguồn đã chia sẻ từ nhóm UndertheSea cũng như những đóng góp của nhóm UndertheSea dành cho cộng đồng.

Dự án sử dụng tập dữ liệu **[VNTC](https://github.com/duyvuleo/VNTC)** và **[Foody](https://streetcodevn.com/blog/dataset)** trong các thử nghiệm. Xin vui lòng kiểm tra lại thông tin trên website hoặc báo cáo khoa học tương ứng để biết thông tin về bản quyền và trích dẫn khi sử dụng tập dữ liệu này.
