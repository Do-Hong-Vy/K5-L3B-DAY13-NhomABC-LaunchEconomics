# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: NhomABC · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.471,97 đ/việc (978/1.200 việc thành công), gấp **16,28×** hoá đơn token+tool 274,65 đ/yc; giờ nhân viên chiếm 92,5% (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại **+51,77%** · 2. Xem lại **+40,70%** · 3. Lương nhân viên **+23,12%** (`simulated`); giới hạn 2 lần chạy rẻ nhất cả hệ thống (6.901.220,23 đ) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Toàn mẫu (cả hệ thống): **5.864,65 đ/yc = 0,49×** của 12.000 đ; phạm vi pilot `noi_dia` (0,22×) + `hang_nang` (0,69×) gồm cố định 40 triệu/tháng: **4.599,09 đ = 0,38×** ở 45k yc/tháng (**5.784,27 đ = 0,48×** ở nửa khối lượng; cả xử lý thủ công 5.217,09 đ/yc, `simulated`); loại `quoc_te` (1,88×) và `doi_tac` (0,85×) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử (chưa có đối chứng): đóng 24h & không mở lại 7 ngày **82,83%** (994/1.200); bỏ qua gợi ý **27,12%** (48/177); mở lại 7 ngày **4,25%** (51/1.200; phạm vi pilot 3,97%); đủ 10 event có `trace_id` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đã chốt 20/20 nhãn thống nhất (5 loại PAIR) và bảng khắc phục 5 ca có ngưỡng đo khớp event `chi_so.md`; chưa có bộ nhãn độc lập thứ hai | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên **20 + 20 nhân viên** (đủ 20 cụm/nhóm), phạm vi `noi_dia + hang_nang`, `m ≥ 299` (5.980 yc thô/nhóm, `n` hiệu dụng 859, `DE = 6,96`), MDE 6 điểm (`power = 0,80`); **power chỉ còn ~0,64 nếu tác động thật là 5 điểm**; 3 luật dừng đủ 4 vế & rollback 30 phút | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2 → **6.786,90 đ (+51,77%)**; xem lại 100% → **11.742,79 đ (0,98×)** ở 9 phút/ca hoặc **12.414,50 đ (1,03×)** ở 15,3 phút/ca (hòa vốn xem lại ≤ 5,1 / 4,8 phút); nửa khối lượng tăng cố định lên **+2.370,37 đ/việc** (`simulated`) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho kế hoạch pilot phạm vi `noi_dia + hang_nang` (loại `quoc_te` và `doi_tac`), chỉ bật pilot khi đáp ứng đủ 4 điều kiện sau:

- **Vá lỗi hệ thống & bật telemetry:** Kỹ sư trưởng agent vá khóa chống hoàn trùng và đối soát sổ cái (ca 7, 20), bật đủ 10 event có `trace_id` (gồm `created_at` và phút đo thật) — *hạn kiểm tra: trước ngày bắt đầu pilot (không muộn hơn 05/01/2027)*.
- **Hoàn tất đánh giá lỗi độc lập:** Kỹ sư trưởng agent và PM trợ lý hoàn phí hoàn tất bộ nhãn độc lập thứ hai trên mẫu kiểm định mới (đồng thuận ≥ 80%) trước khi mở rộng rollout — *hạn kiểm tra: trước bước rollout `0.25`*.
- **Chấp nhận đánh đổi thống kê:** Giám đốc vận hành ký chấp nhận MDE 6 điểm (`power ≈ 0,64` nếu tác động thật chỉ 5 điểm) và giữ nguyên 3 luật dừng 4 vế — *hạn kiểm tra: trước ngày bắt đầu pilot*.
- **Kiểm soát chi phí xem lại thực tế:** Trưởng nhóm CSKH thay toàn bộ phút `simulated` bằng phút đo thật từ tuần 1 và áp dụng lộ trình hạ tỉ lệ xem lại theo bậc (vì xem lại 100% tốn 11.742,79–12.414,50 đ/việc, `simulated`, không còn tiết kiệm); PM trợ lý hoàn phí rà soát chi phí đo thật trước ngày quyết định *05/01/2027*.
