# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Hà Nam · Người gắn nhãn 2: Nguyễn Trung Dũng. Người gắn nhãn 2 đã xem đáp án và nhãn người 1; chưa có bộ nhãn tự đánh giá và chưa thể ghi nhận hai bộ nhãn độc lập.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn đề xuất, chờ thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Chờ | Chờ | Do người dùng |
| 2 | Hệ thống | Chờ | Chờ | Hệ thống |
| 3 | Ngữ cảnh | Chờ | Chờ | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Chờ | Chờ | Giới hạn hệ thống |
| 5 | Ngầm | Chờ | Chờ | Ngầm |
| 6 | Do người dùng | Chờ | Chờ | Do người dùng |
| 7 | Hệ thống | Chờ | Chờ | Hệ thống |
| 8 | Hệ thống | Chờ | Chờ | Hệ thống |
| 9 | Do người dùng | Chờ | Chờ | Do người dùng |
| 10 | Ngữ cảnh | Chờ | Chờ | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Chờ | Chờ | Giới hạn hệ thống |
| 12 | Ngầm | Chờ | Chờ | Ngầm |
| 13 | Giới hạn hệ thống | Chờ | Chờ | Giới hạn hệ thống |
| 14 | Do người dùng | Chờ | Chờ | Do người dùng |
| 15 | Hệ thống | Chờ | Chờ | Hệ thống |
| 16 | Ngữ cảnh | Chờ | Chờ | Ngữ cảnh |
| 17 | Ngầm | Chờ | Chờ | Ngầm |
| 18 | Ngữ cảnh | Chờ | Chờ | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Chờ | Chờ | Giới hạn hệ thống |
| 20 | Hệ thống | Chờ | Chờ | Hệ thống |

**Tỉ lệ đồng thuận:** Chưa tính được do chưa có hai bộ nhãn độc lập. Cột đề xuất dựa trên nhãn tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và cần Nam và Dũng xác nhận trước khi coi là thống nhất.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Chờ hai người gắn nhãn xem lại và xác nhận các nhãn thống nhất.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Theo dõi `handoff_to_staff` với lý do mã không hợp lệ hằng ngày; cảnh báo nếu quá 2% yêu cầu | Hướng dẫn tìm mã vận đơn hoặc chuyển nhân viên nếu không tra được | Người phụ trách sản phẩm |
| 7 | Hệ thống | Đối soát `refund_ledger_write` hằng giờ với thông báo thành công; ngưỡng 0 ca lệch | Chỉ báo hoàn thành khi sổ cái xác nhận; sau 3 lần lỗi thì chuyển nhân viên | Kỹ sư phụ trách trợ lý |
| 18 | Ngữ cảnh | Theo dõi `ticket_reopened` hằng tuần và kiểm tra các ca nghi hoàn thiếu | Ghi rõ số tiền gốc, tỉ lệ hoàn và phép tính trong thông báo | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Đếm `handoff_to_staff` vì thiếu dữ liệu theo tuần và loại yêu cầu | Chuyển nhân viên kèm tóm tắt; không đưa yêu cầu quốc tế vào pilot | Người phụ trách sản phẩm |
| 17 | Ngầm | Dùng `audit_sample_checked` kiểm tra 100 đơn/tuần với bảng giá hiện hành; cảnh báo nếu từ 1% đơn bị lệch | Cập nhật bộ nhớ đệm khi đổi giá và lưu phiên bản bảng giá | Kế toán trưởng |
