# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng (tự đề xuất) | Tỉ lệ chấp nhận mở trợ lý ở nhóm can thiệp | Số yêu cầu thuộc nhóm can thiệp (`arm = treatment`) có event `agent_suggestion_shown` chia tổng số yêu cầu trong phạm vi của nhóm can thiệp | Không cần tính |
| An toàn (tự đề xuất) | Tỉ lệ đơn hoàn sai số tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm) | Số đơn có `so_tien_da_hoan != so_tien_dung` chia tổng số đơn được kiểm tra mẫu (`audit_sample_checked`, 100 đơn/tuần) | Không cần tính |

Chỉ số trong đợt chạy thử là **82,83%** (994/1.200) cho chỉ số chính, **27,12%** (48/177) cho tỉ lệ bỏ qua gợi ý, và **4,25%** (51/1.200; trong phạm vi `noi_dia` + `hang_nang` là **3,97%**) cho tỉ lệ mở lại trong 7 ngày. Không kết luận trợ lý đã nâng chỉ số vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event cốt lõi, mọi event đều gắn `trace_id` để nối với trace của agent và đo thời gian nhân viên thực tế (thay cho số `simulated` từ tuần 1 của pilot):

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách hàng | `request_id`, `loai`, `so_tien_vnd`, `depot`, `arm`, `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy của agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `arm`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Giao diện nhân viên | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Giao diện nhân viên | `request_id`, `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất xử lý làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang nhân viên xử lý |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | App khách / CSKH | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu sau khi đã đóng |
| `audit_sample_checked` | Hệ thống kiểm toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `phien_ban_bang_gia`, `trace_id` | Khi kế toán kiểm tra mẫu 100 đơn/tuần |

**Kiểm tra chéo:** mọi chỉ số ở bảng E1 đều tính được trực tiếp từ danh sách event trên bằng cách đếm theo `request_id` duy nhất và nối trace qua `trace_id`:

- **Chỉ số chính (% đóng trong 24h và không mở lại trong 7 ngày):** `refund_request_created` (mốc tạo, tổng yêu cầu), `ticket_closed` (kiểm tra `closed_at - created_at ≤ 24h`) và `ticket_reopened` (không có event trong 7 ngày kể từ `closed_at`).
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý):** `staff_review_decision` (đếm `quyet_dinh` thuộc `sua` hoặc `bo` chia tổng số event `staff_review_decision`).
- **Chỉ số an toàn (tỉ lệ mở lại trong 7 ngày):** `refund_request_created` (tổng yêu cầu) và `ticket_reopened` (số yêu cầu có `reopened_at - closed_at ≤ 7 ngày`).
- **Chỉ số dùng tự đề xuất (% yêu cầu nhóm can thiệp mở bằng trợ lý):** `refund_request_created` (lọc `arm = treatment`, phạm vi pilot) và `agent_suggestion_shown`.
- **Chỉ số an toàn tự đề xuất (% đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần):** `audit_sample_checked` (so sánh `so_tien_da_hoan` với `so_tien_dung`, đối chiếu thêm `refund_ledger_write` theo `trace_id`).
- **Chi phí mỗi việc thành công đo thật (thay số `simulated`):** `agent_run_completed` (token + tool mọi lần chạy), `staff_review_decision` (`phut_xem_lai`), `staff_rework_completed` (`phut_lam_lai`), `ticket_closed` & `ticket_reopened` (đếm việc thành công).

## E2 · Rủi ro kinh tế

Số liệu tác động lấy trực tiếp từ bảng chi phí và bảng độ nhạy (`bang_chi_phi.md` / `src/lab13.py`), toàn bộ số từ cột `_simulated` ghi rõ nhãn `simulated`:

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất, #1 bảng B1) | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** (`simulated`) | Tỉ lệ ca làm lại theo tuần (`staff_rework_completed`) vượt **7%** (đợt chạy thử trong phạm vi `noi_dia` + `hang_nang` là **4,89%**, 48/982 ca) | Thu hẹp phạm vi về chỉ `noi_dia` và rà soát 20 trace `staff_rework_completed` gần nhất để vá nguyên nhân gốc | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài hoặc thời gian xem lại vượt ngưỡng hoà vốn (B4) | Trong phạm vi `noi_dia` + `hang_nang`, chi phí tăng lên **11.743 đ = 0,98×** baseline 12.000 đ (với 9 phút/ca làm lại) hoặc **12.415 đ = 1,03×** (với trung bình dữ liệu 15,3 phút/ca) (`simulated`) — đắt hơn nhân viên tự làm; hoà vốn đòi hỏi xem lại ≤ **5,1 phút** (hoặc ≤ **4,8 phút**) | Tỉ lệ yêu cầu được xem lại vẫn **> 50%** vào cuối bước rollout `0.25`, hoặc `phut_xem_lai` trung bình (đo thật từ `staff_review_decision`) **> 4,8 phút** trong 1 tuần | Triển khai hạ tỉ lệ xem lại theo bậc khi tỉ lệ `sua + bo < 15%`, đồng thời rút gọn giao diện đối chiếu để giảm thời gian xem lại dưới 4 phút | Trưởng nhóm CSKH |
| Khối lượng xử lý thấp hơn kế hoạch làm đội chi phí cố định (A4) | Chi phí cố định 40 triệu đ/tháng cộng thêm **+1.185 đ/việc** ở 45.000 yc/tháng (CPS = **4.599 đ = 0,38×**), tăng gấp đôi lên **+2.370 đ/việc** khi khối lượng còn một nửa (CPS = **5.784 đ = 0,48×**) (`simulated`) | Số việc thành công theo tuần đạt **< 50%** kế hoạch của bước rollout hiện tại trong 2 tuần liên tiếp | Giữ nguyên bước rollout, chưa mở rộng sang nhóm mới và rà soát lại cơ cấu chi phí cố định hằng tháng trước ngày quyết định | PM trợ lý hoàn phí |
