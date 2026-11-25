# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Nhãn tham khảo

Tổng hợp từ mục “Nhãn tham khảo cho 20 ca” trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, có dùng Codex để đọc và ghi lại. Đây là đáp án tham khảo, không phải bằng chứng hai người đã gắn nhãn độc lập.

| Loại lỗi | Ca |
| --- | --- |
| Do người dùng | 1, 6, 9, 14 |
| Hệ thống | 2, 7, 8, 15, 20 |
| Ngữ cảnh | 3, 10, 16, 18 |
| Giới hạn hệ thống | 4, 11, 13, 19 |
| Ngầm | 5, 12, 17 |

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Hà Nam · Người gắn nhãn 2: Nguyễn Trung Dũng. Cột người 2 chép từ nhãn tham khảo với hỗ trợ của Codex sau khi đã xem đáp án và bộ nhãn người 1; không phải bộ nhãn gắn độc lập.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | ... |
| 2 | Hệ thống | Hệ thống | Có | ... |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | ... |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | ... |
| 5 | Ngầm | Ngầm | Có | ... |
| 6 | Do người dùng | Do người dùng | Có | ... |
| 7 | Hệ thống | Hệ thống | Có | ... |
| 8 | Hệ thống | Hệ thống | Có | ... |
| 9 | Do người dùng | Do người dùng | Có | ... |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | ... |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | ... |
| 12 | Ngầm | Ngầm | Có | ... |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | ... |
| 14 | Do người dùng | Do người dùng | Có | ... |
| 15 | Hệ thống | Hệ thống | Có | ... |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | ... |
| 17 | Ngầm | Ngầm | Có | ... |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | ... |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | ... |
| 20 | Hệ thống | Hệ thống | Có | ... |

**Tỉ lệ trùng:** 20 / 20 = 100%; đây không phải tỉ lệ đồng thuận giữa hai lượt gắn nhãn độc lập vì cột người 2 dùng đáp án tham khảo.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca khác nhãn trong hai cột hiện tại; nhãn thống nhất cần hai thành viên xác nhận.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Theo dõi event nhập mã không hợp lệ hằng ngày; cảnh báo nếu quá 2% yêu cầu | Hướng dẫn tìm mã vận đơn hoặc chuyển nhân viên nếu không tra được | Người phụ trách sản phẩm |
| 7 | Hệ thống | Đối soát hằng giờ thông báo thành công với sổ cái; ngưỡng 0 ca lệch | Chỉ báo hoàn thành khi sổ cái xác nhận; sau 3 lần lỗi thì chuyển nhân viên | Kỹ sư phụ trách trợ lý |
| 18 | Ngữ cảnh | Theo dõi hằng tuần và kiểm tra các ca mở lại vì nghi hoàn thiếu | Ghi rõ số tiền gốc, tỉ lệ hoàn và phép tính trong thông báo | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Đếm event chuyển nhân viên vì thiếu dữ liệu theo tuần và loại yêu cầu | Chuyển nhân viên kèm tóm tắt; không đưa yêu cầu quốc tế vào pilot | Người phụ trách sản phẩm |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần với bảng giá hiện hành; cảnh báo nếu từ 1% đơn bị lệch | Cập nhật bộ nhớ đệm khi đổi giá và lưu phiên bản bảng giá | Kế toán trưởng |
