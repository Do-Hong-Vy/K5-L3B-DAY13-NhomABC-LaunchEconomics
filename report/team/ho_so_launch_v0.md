# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: NhomABC · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.471,97 đ/việc (978/1.200 việc thành công), gấp **16,28×** hoá đơn token+tool 274,65 đ/yc; giờ nhân viên chiếm 92,5% (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại **+51,77%** · 2. Xem lại **+40,70%** · 3. Lương nhân viên **+23,12%** (`simulated`); giới hạn 2 lần chạy rẻ nhất cả hệ thống (6.901.220,23 đ) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Toàn mẫu (cả hệ thống): **5.864,65 đ/yc = 0,49×** của 12.000 đ; phạm vi pilot `noi_dia` (0,22×) + `hang_nang` (0,69×) gồm cố định 40 triệu/tháng: **4.599,09 đ = 0,38×** ở 45k yc/tháng (**5.784,27 đ = 0,48×** ở nửa khối lượng; cả xử lý thủ công 5.217,09 đ/yc, `simulated`); loại `quoc_te` (1,88×) và `doi_tac` (0,85×) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử (chưa có đối chứng): đóng 24h & không mở lại 7 ngày **82,83%** (994/1.200); bỏ qua gợi ý **27,12%** (48/177); mở lại 7 ngày **4,25%** (51/1.200; phạm vi pilot 3,97%); đủ 10 event có `trace_id` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đã chốt 20/20 nhãn thống nhất (5 loại PAIR) và bảng khắc phục 5 ca có ngưỡng đo khớp event `chi_so.md`; chưa có bộ nhãn độc lập thứ hai | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên **20 + 20 nhân viên** (đủ 20 cụm/nhóm), phạm vi `noi_dia + hang_nang`, `m ≥ 299` (5.980 yc thô/nhóm, `n` hiệu dụng 859, `DE = 6,96`), MDE 6 điểm (`power = 0,80`; **power ~0,64 nếu tác động chỉ 5 điểm**); chạy `30/11–31/12/2026` (gồm bước `0.50` 10 ngày gom mẫu + 7 ngày bảo hành), quyết định `05/01/2027`; 4 luật dừng 4 vế (lệch +2 điểm từ 10 người; ngưỡng 8.000 đ chỉ tính chi phí biến đổi; xem lại ≤ 4,8 phút & ≤ 50%) & rollback 30 phút | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2 → **6.786,90 đ (+51,77%)**; xem lại 100% → **11.742,79 đ (0,98×)** ở 9 phút/ca hoặc **12.414,50 đ (1,03×)** ở 15,3 phút/ca (hòa vốn xem lại ≤ 5,1 / 4,8 phút); nửa khối lượng tăng cố định lên **+2.370,37 đ/việc** (`simulated`) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho kế hoạch pilot phạm vi `noi_dia + hang_nang` (loại `quoc_te` và `doi_tac`), bắt đầu **30/11/2026**, tổng hợp và quyết định **05/01/2027** (chỉ bật pilot khi đáp ứng đủ 4 điều kiện sau; nếu trễ hạn `28/11` thì lùi đồng thời ngày bắt đầu và ngày quyết định giữ đủ 31 ngày chạy + 5 ngày đệm):

- **Điều kiện 1 · Vá lỗi hệ thống & bật telemetry:** Kỹ sư trưởng agent vá khóa chống hoàn trùng (ca 20) và đối soát sổ cái (ca 7), bật đủ 10 event có `trace_id` (gồm `created_at` và phút đo thật) — *kiểm tra: 28/11/2026 (trước khi bật pilot)*.
- **Điều kiện 2 · Hoàn tất đánh giá lỗi độc lập:** PM trợ lý hoàn phí tổ chức hoàn tất bộ nhãn độc lập thứ hai trên mẫu kiểm định mới đạt đồng thuận ≥ 80% — *kiểm tra: 07/12/2026 (trước khi lên bước `0.25`)*.
- **Điều kiện 3 · Chấp nhận đánh đổi thống kê:** Giám đốc vận hành ký chấp nhận MDE 6 điểm (`power ≈ 0,64` nếu tác động thật chỉ 5 điểm), lịch pilot `30/11–31/12/2026` và 4 luật dừng 4 vế — *kiểm tra: 28/11/2026 (trước khi bật pilot)*.
- **Điều kiện 4 · Kiểm soát thời gian & tỉ lệ xem lại đo thật:** Trưởng nhóm CSKH thay toàn bộ phút `simulated` bằng phút đo thật từ tuần 1, đạt trung bình ≤ 4,8 phút/lần xem lại và tỉ lệ được xem lại ≤ 50% (hạ bậc khi `sua + bo < 15%`, vì xem lại 100% tốn 11.742,79–12.414,50 đ/việc, `simulated`); chưa đạt không mở bước `0.50` — *kiểm tra tuần 1: 07/12/2026, chốt bước `0.50`: 14/12/2026*.
