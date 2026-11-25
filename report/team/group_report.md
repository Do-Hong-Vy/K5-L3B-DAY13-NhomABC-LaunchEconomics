# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: NhomABC · Lớp: L3B
- Thành viên và vai trò: xem `TEAM.md`.

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá chi phí, lỗi và kế hoạch pilot của trợ lý hoàn phí LogiX-VN dựa trên mẫu 1.200 yêu cầu và 1.624 lần chạy. Chi phí có dùng thời gian nhân viên giả lập; kết quả chạy thử chưa có nhóm đối chứng.

## 3. Giải pháp

- **Nhiệm vụ A–B:** cài đặt mô hình chi phí, tách theo loại yêu cầu, cộng chi phí cố định và chạy 9 kịch bản độ nhạy + chi phí cả hệ thống + xem lại 100% trong `src/lab13.py`, đối chiếu độc lập và tổng hợp tại [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C:** phân loại 20 ca lỗi theo 5 nhóm Google PAIR (nguyên nhân gốc), chốt nhãn thống nhất và xây bảng khắc phục 5 ca gắn event đo được tại [bang_loi.md](bang_loi.md) (ghi nhận trung thực việc thiếu bộ nhãn độc lập thứ hai).
- **Nhiệm vụ D:** tính 5 câu cỡ mẫu D1 trong `src/lab13.py`, kiểm tra 5 câu tách tác động D2 và viết kế hoạch pilot có đối chứng cùng 3 luật dừng 4 vế tại [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E & Duyệt chéo:** tính thử 3 chỉ số, thiết kế 10 event có `trace_id` và 3 dòng rủi ro kinh tế tại [chi_so.md](chi_so.md); tổng hợp hồ sơ 1 trang tại [ho_so_launch_v0.md](ho_so_launch_v0.md) và ghi phiếu chấm hội đồng tại [phieu_cham.md](phieu_cham.md).

## 4. Kết quả

- **Kinh tế & độ nhạy (`simulated`):** Chi phí mỗi việc thành công là **4.471,97 đ** (978/1.200 việc), gấp **16,28×** hoá đơn token+tool (274,65 đ/yc); chi phí cả hệ thống công bằng là **5.864,65 đ/yc (0,49×** so với 12.000 đ). Trong phạm vi pilot `noi_dia + hang_nang`, chi phí gồm cố định 40 triệu đ/tháng là **4.599,09 đ (0,38×)** ở 45.000 yc/tháng và **5.784,27 đ (0,48×)** ở nửa khối lượng; loại `quoc_te` (1,88×) và `doi_tac` (0,85×). Ba yếu tố nhạy nhất là số ca làm lại (+51,77%), tỉ lệ xem lại (+40,70%) và lương nhân viên (+23,12%); giới hạn **2 lần chạy** rẻ nhất cả hệ thống (**6.901.220,23 đ**); xem lại 100% tốn **11.742,79–12.414,50 đ/việc** (0,98×–1,03×, không còn tiết kiệm).
- **Chỉ số đợt chạy thử (không đối chứng):** đóng trong 24h & không mở lại 7 ngày **82,83%** (994/1.200); bỏ qua gợi ý **27,12%** (48/177); mở lại trong 7 ngày **4,25%** (51/1.200; phạm vi pilot 3,97%).
- **Kế hoạch pilot & đề xuất:** chia ngẫu nhiên **20 + 20 nhân viên**, `m ≥ 299` (5.980 yc thô/nhóm, `DE = 6,96`), MDE **6 điểm** (`power = 0,80`; nếu tác động thật chỉ 5 điểm thì `power ≈ 0,64`). Đề xuất cuối trong [ho_so_launch_v0.md](ho_so_launch_v0.md): **Go có điều kiện**.
- **Kết quả nhóm nhận được từ hội đồng Gate 2a:** *(sẽ cập nhật ngay sau phiên duyệt chéo 17:00–17:45)*.

## 5. Khó khăn và cách xử lý

Mẫu chỉ có 40 nhân viên, nên chia theo nhân viên không đủ power 0,80 để phát hiện chênh lệch 5 điểm. Kế hoạch chấp nhận mức chênh 6 điểm (`power ≈ 0,64` ở mức 5 điểm), chốt 3 luật dừng đủ 4 vế và yêu cầu bật đủ 10 event có `trace_id` để thay phút giả lập bằng phút đo thật từ tuần 1 của pilot.

## 6. Tổng hợp đóng góp

Vai trò, phần việc và bằng chứng PR/commit của cả 4 thành viên được ghi chi tiết trong [TEAM.md](../../TEAM.md) và 4 báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

Thời gian xem lại và làm lại là `simulated`; cần đo thực tế từ tuần 1 của pilot qua `staff_review_decision` và `staff_rework_completed`. Nhóm chưa có hai bộ nhãn lỗi độc lập ở nhiệm vụ C nên chưa tính được tỉ lệ đồng thuận; cần thực hiện gắn nhãn độc lập trên mẫu kiểm định mới trước bước rollout `0.25`. Đợt chạy thử không có nhóm đối chứng nên chỉ báo cáo số liệu quan sát, không kết luận tác động nhân quả.

## 8. Tài liệu tham khảo

- Dữ liệu, công thức và hướng dẫn trong thư mục `docs/` của repo (`du_lieu_va_cong_thuc.md`, `Lab13_Huong_dan_chi_tiet_buoi_chieu.md`).
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, phần Errors + Graceful Failure: https://pair.withgoogle.com/guidebook/chapters/errors-failures/
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`statsmodels.stats.power`).
