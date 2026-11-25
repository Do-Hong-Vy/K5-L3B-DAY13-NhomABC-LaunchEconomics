# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Hà Nam · Người gắn nhãn 2: Nguyễn Trung Dũng. Người gắn nhãn 2 đã xem nhãn tham khảo và nhãn người 1; chưa có hai bộ nhãn độc lập.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
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

**Tỉ lệ đồng thuận:** Chưa tính được vì chưa có hai bộ nhãn độc lập. Dũng chốt nhãn thống nhất dựa trên hướng dẫn trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, theo quyền Nam đã giao.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Chưa có bộ nhãn độc lập thứ hai để xác định các ca không trùng giữa hai người gắn nhãn.
- Quy tắc phân biệt theo nguyên nhân gốc nhóm áp dụng cho các ca dễ lẫn khi chốt cột `Nhãn thống nhất`:
  - **Do người dùng vs Hệ thống (ca 6, 9):** gốc lỗi do khách chọn sai mục hoặc nhập sai mã thì gắn `Do người dùng`; việc trợ lý chưa tự gợi ý là hành động cải thiện ở cột khắc phục.
  - **Giới hạn hệ thống (ca 13):** yêu cầu ngoài phạm vi hoặc thiếu dữ liệu nguồn luôn là `Giới hạn hệ thống`, kể cả khi trợ lý xử lý tình huống chuyển tiếp chưa tốt.
  - **Hệ thống vs Ngầm (ca 8, 12, 15):** sai đã lộ ra cho khách hoặc nhân viên thấy (ca 8, 15) là `Hệ thống`; chỉ gắn `Ngầm` khi không ai phát hiện cho tới khi kiểm tra mẫu hoặc đối soát chi phí (ca 5, 12, 17).
  - **Ngữ cảnh (ca 18):** số tiền hoàn đúng chính sách nhưng giả định khách tự hiểu cách tính không khớp hoàn cảnh thực tế thì gắn `Ngữ cảnh`.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Theo dõi `handoff_to_staff` có `reason = ma_khong_hop_le` theo `trace_id` hằng ngày; cảnh báo khi > 2% tổng yêu cầu/ngày | Tự nhận diện mã sàn TMĐT để tra mã vận đơn; không tra được thì hướng dẫn kèm ảnh và chuyển nhân viên | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát `refund_ledger_write` hằng giờ theo `trace_id` với thông báo "đã hoàn"; ngưỡng cảnh báo 0 ca lệch | Chỉ báo hoàn thành khi sổ cái trả `ok` kèm `idempotency_key`; sau 3 lần lỗi báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi `ticket_reopened` có lý do nghi hoàn thiếu hằng tuần theo `trace_id` (nhưng kiểm tra thấy đúng chính sách); rà soát từ ≥ 1 ca/tuần | Mẫu tin nhắn luôn ghi rõ số tiền gốc, tỉ lệ hoàn và phép tính cụ thể (ví dụ `30.000 đ × 50% = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Đếm `handoff_to_staff` có `reason = thieu_du_lieu` theo tuần và theo `loai` qua `trace_id`; rà soát từ ≥ 1 ca ở phạm vi pilot | Chuyển nhân viên kèm tóm tắt ngữ cảnh; loại `quoc_te` và `doi_tac` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Dùng `audit_sample_checked` kiểm tra mẫu 100 đơn/tuần theo `trace_id` đối chiếu bảng giá hiện hành; cảnh báo khi ≥ 1% đơn lệch tiền | Xoá bộ nhớ đệm ngay khi có bảng giá mới và lưu `phien_ban_bang_gia` vào trace | Kế toán trưởng |
