# Báo cáo cá nhân — Lê Khánh Cường — 2A202603999

Báo cáo ghi lại phần việc của tôi trong Lab 13, tính đến ngày 25/11/2026. Bảng chi phí CP1–CP2 và code CP4 đã được merge. Phần kiểm số chỉ số, kế hoạch pilot và hồ sơ launch đã có nhận xét trên GitHub; một số điểm về cách đo và cập nhật hồ sơ còn cần nhóm xử lý.

## 1. Thông tin thành viên

- Họ tên: Lê Khánh Cường.
- MSSV: 2A202603999.
- Email: 26ai.cuonglk2@vinuni.edu.vn.
- GitHub: `lekhanhcuongvk1`.
- Nhóm: NhomABC; lớp: L3B.
- Vai: người kiểm số CP1–CP2; nhận phần viết code cỡ mẫu CP4 theo phân công đổi vai trong `task.md`.

## 2. Phần việc phụ trách

- CP1: kiểm số độc lập từ hai CSV, hoàn thiện A1–A4 trong [bảng chi phí](bang_chi_phi.md).
- CP2: kiểm tra chín kịch bản độ nhạy, tác động ghép, giới hạn chạy lại và xem lại 100%; điền B1–B4 cùng cách tính.
- CP4: bổ sung phần tính D1a–e, power và tỷ lệ mở lại trong `src/lab13.py`; cung cấp kết quả cho Nam viết kế hoạch pilot.
- Tôi đã review YAML của Nam, kiểm số chỉ số và hồ sơ launch, đồng thời ghi nhận các điểm cần làm rõ trên GitHub. Việc tham gia duyệt chéo và review phiếu chấm chưa hoàn tất tại thời điểm viết báo cáo.

## 3. Đóng góp cụ thể

Tôi phụ trách bảng chi phí và phần code cỡ mẫu, có sử dụng Codex để hỗ trợ tính toán, viết code và kiểm tra kết quả. Bảng dưới đây tóm tắt những nội dung đã có trong các PR của tôi.

| Phần | Nội dung và kết quả có bằng chứng | Trạng thái |
| --- | --- | --- |
| CP1 | Điền A1–A4, công thức và đầu vào kiểm chứng; CPS 4.471,97 đ, chi phí hệ thống 5.864,65 đ/yêu cầu [simulated]. Công cụ thực hiện 83 phép so với code Vỹ, kết quả khớp trong sai số số thực. | PR #6 đã merge |
| CP2 | Đủ B1–B4; số ca làm lại là yếu tố ảnh hưởng mạnh nhất trong các kịch bản (+51,77% [simulated]); giới hạn 2 lần chạy có tổng hệ thống thấp nhất, 6.901.220,23 đ [simulated]. | PR #7 đã merge |
| CP2 — B4 | Ghi rõ xem lại 100% tốn 11.742,79 hoặc 12.414,50 đ/việc thành công [simulated], tùy thời gian làm lại 9 phút hoặc trung bình chưa làm tròn 15,2973 phút/ca [simulated]. Giải thích khác biệt hiển thị do làm tròn. | Có trong bảng chi phí |
| CP4 | Viết code tính 1.251 mẫu/nhóm cho MDE 5 điểm; chia theo nhân viên với m=75 cần DE 2,48, 3.103 yêu cầu và 42 người/nhóm, vượt tổng 40 người có sẵn. | PR #9 đã merge |
| CP4 — đánh đổi | Với 20 nhân viên/nhóm, MDE 6 điểm cần 859 mẫu hiệu dụng/nhóm, m ≥ 299, DE 6,96; power khoảng 0,6417 nếu tác động thật chỉ 5 điểm. Baseline mở lại là 51/1.200 = 4,25%; trong phạm vi là 39/982 = 3,97%. | Đã có trong code và đối chiếu với YAML |
| Review hồ sơ | Kiểm lại ba chỉ số từ CSV, tác động kinh tế, cỡ mẫu trong YAML và số liệu hồ sơ launch; ghi nhận các điểm về timestamp, đếm yêu cầu duy nhất, thời gian theo dõi 7 ngày và mục pilot chưa cập nhật. | Có ba nhận xét kiểm số trên GitHub |

## 4. Bằng chứng

| PR | File / commit thay đổi | Trạng thái được kiểm tra ngày 25/11/2026 |
| --- | --- | --- |
| [#6 — Kiểm số CP1](https://github.com/Do-Hong-Vy/K5-L3B-DAY13-NhomABC-LaunchEconomics/pull/6) | `report/team/bang_chi_phi.md`; commit `394ff7a` | Đã merge, commit merge `91d67e3` |
| [#7 — Bảng độ nhạy CP2](https://github.com/Do-Hong-Vy/K5-L3B-DAY13-NhomABC-LaunchEconomics/pull/7) | `report/team/bang_chi_phi.md`; commit `89b5df8` | Đã merge, commit merge `70af75b` |
| [#9 — Code cỡ mẫu CP4](https://github.com/Do-Hong-Vy/K5-L3B-DAY13-NhomABC-LaunchEconomics/pull/9) | `src/lab13.py`; commit `576fa71` | Đã merge, commit merge `eef14af` |

Nhận xét kiểm số sau khi cập nhật `main` đến `b084e1a`:

- [Chỉ số và rủi ro kinh tế của Vỹ, PR #3](https://github.com/Do-Hong-Vy/K5-L3B-DAY13-NhomABC-LaunchEconomics/pull/3#issuecomment-7157580366): số liệu khớp; cần bổ sung mốc thời gian, quy tắc đếm yêu cầu duy nhất và cách xác nhận không sai tiền.
- [Kế hoạch pilot của Nam, commit b084e1a](https://github.com/Do-Hong-Vy/K5-L3B-DAY13-NhomABC-LaunchEconomics/commit/b084e1a01375e308346b4c3e86630208e2a4bc12#commitcomment-211768720): YAML hợp lệ và khớp D1; cần làm rõ tập yêu cầu đủ 7 ngày theo dõi, lịch thu mẫu, giám sát vận hành và việc dùng phút đo thật.
- [Hồ sơ launch của Dũng, PR #8](https://github.com/Do-Hong-Vy/K5-L3B-DAY13-NhomABC-LaunchEconomics/pull/8#issuecomment-7157581788): số liệu khớp; mục pilot cần cập nhật theo YAML mới, còn trạng thái Chưa của bảng nhãn lỗi phù hợp với bằng chứng hiện có.

- CP1: đọc CSV bằng `csv.DictReader`, tính tiền bằng `decimal.Decimal`, đối chiếu giá trị chưa làm tròn với `mo_hinh`; 83 phép so đạt (`rel_tol=1e-12`, `abs_tol=1e-8`).
- CP2: 55 phép so đạt và 4 kiểm tra tuyến tính đạt; kiểm tra đầu vào/tổng/CPS/ngưỡng hòa vốn B4 với output. Chi tiết công thức nằm trong [bảng chi phí](bang_chi_phi.md).
- CP4: kiểm tra công thức cỡ mẫu và power độc lập bằng SciPy; m=298 chưa đạt nhưng m=299 đạt 859 hiệu dụng/nhóm; đếm lại tỷ lệ mở lại từ CSV.
- Kết quả chạy qua Codex trên workspace: `python lab13.py` trong `src/` hoàn tất; ba phép thử A1 và các kiểm tra tuyến tính B đạt, output A–B–E giữ nguyên khi thêm CP4; `git diff --check` đạt.
- Bằng chứng hiện tại gồm các phép tính bằng chương trình và kết quả đối chiếu. Báo cáo chưa ghi nhận phần kiểm tay riêng hoặc xác nhận chạy trên hai máy khác nhau.
- Phiếu chấm vẫn là mẫu tại thời điểm review; chưa có hồ sơ nhóm được chấm hoặc kết quả hội đồng để đối chiếu.

## 5. Công cụ AI đã dùng

Tôi dùng Codex để đọc yêu cầu lab, hỗ trợ tính từ CSV, điền bảng chi phí và viết code cỡ mẫu. Công cụ cũng hỗ trợ chạy kiểm tra, quản lý nhánh, commit, push và tạo PR.

Cách kiểm tra trong phần việc này là tính lại bằng `csv`/`Decimal`, rồi đối chiếu với code pandas của Vỹ; riêng cỡ mẫu và power được kiểm tra chéo bằng SciPy. Việc so output trước và sau khi thêm CP4 giúp xác nhận các phần A–B–E vẫn giữ nguyên.

Các phép kiểm trên được thực hiện qua công cụ. Phần tự kiểm bằng tay của tôi chưa được ghi nhận trong báo cáo. Những phép tính quan trọng đã được trình bày rõ trong bảng chi phí, chẳng hạn 4.093.220,23 + 234 × 12.000 = 6.901.220,23 đ [simulated] và DE = 1 + (299 − 1) × 0,02 = 6,96.

## 6. Tự đánh giá

Về tiến độ, hai PR bảng chi phí và PR code CP4 của tôi đã được merge. Phần kiểm tra bằng chương trình cho kết quả khớp với code của Vỹ và các giá trị đối chiếu của lab. Các nhận xét kiểm số tiếp theo đã được ghi trên GitHub để nhóm đối chiếu khi chốt hồ sơ.

Các số cỡ mẫu đã được đưa đúng vào YAML. Phần còn lại là theo dõi các góp ý về cách đo, kiểm tra hồ sơ launch sau cập nhật và tham gia duyệt chéo. Bằng chứng tự kiểm tay và xác nhận chạy trên máy thứ hai cũng còn thiếu trong báo cáo hiện tại.

Tôi chưa đưa ra tự đánh giá cuối cùng vì phần review hồ sơ và duyệt chéo chưa hoàn tất.
