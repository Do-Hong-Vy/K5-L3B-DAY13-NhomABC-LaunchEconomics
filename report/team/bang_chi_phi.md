# Bảng chi phí · Nhiệm vụ A và B

CP1 do Lê Khánh Cường tính độc lập từ hai CSV bằng Python chuẩn (`csv`, `decimal`), không gọi `src/lab13.py`. Đây là phép kiểm số có AI hỗ trợ; Cường cần tự kiểm chứng các phép tính dưới đây trước khi xác nhận.

**Trạng thái: Đã đối chiếu bằng công cụ với output CP1 của Vỹ ngày 25/11/2026.** CP1 đã merge tại `c0be8ea` (PR #1); bản kiểm tra là `9f76372` sau khi cập nhật `origin/main`. Code chạy hết, ba phép thử A1 đạt; kết quả A2–A4 khớp phép tính độc lập bên dưới. Cường vẫn cần tự kiểm chứng phép tính và xác nhận phần đóng góp cá nhân.

Giá theo đề: token vào 26 đ/1.000, token ra 130 đ/1.000, tool 15 đ/lần, nhân viên 2.000 đ/phút; tự làm 12.000 đ/yêu cầu. Mọi số suy ra từ cột `_simulated` ghi nhãn `simulated`; số tiền làm tròn 2 chữ số, tính toán giữ số chưa làm tròn. Phần B được bổ sung ở CP2, sau khi bảng CP1 của Cường merge qua PR #6 (`91d67e3`).

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | (1 − 0,2²) / 0,8 = **1,20** |
| Số lần chạy trung bình, chạy đến khi đúng | 1 / 0,8 = **1,25** |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | [(1 − 0,2³) / 0,8] / (1 − 0,2³) = 1,24 / 0,992 = **1,25** |

Ba phép tính độc lập khớp giá trị yêu cầu; chạy `python lab13.py` trong `src/` tại `9f76372` in **Ba phép thử đáp án biết trước: ĐẠT**, với 1,20 · 1,25 · 1,25. Công thức giả định xác suất đúng mỗi lần là p cố định; dữ liệu thực tế ở A3 cần kiểm tra riêng theo lần thử.

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585,13 | 5.771.712 token vào × 26/1.000 + 734.774 token ra × 130/1.000 | đo từ trace |
| Tool | 84.000,00 | 5.600 lần gọi × 15 | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804,49 | token + tool của các dòng `attempt > 1`; đã nằm trong hai dòng trên | đo từ trace |
| Xem lại | 1.780.000,00 | 890 phút × 2.000 | simulated |
| Làm lại | 2.264.000,00 | 1.132 phút × 2.000 | simulated |
| Tổng chi phí | 4.373.585,13 | token + tool + xem lại + làm lại; không cộng lại dòng chạy lại | simulated |
| Số việc thành công | 978 | đếm `ket_qua == 'thanh_cong'` (đơn vị: yêu cầu) | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.471,97 | 4.373.585,132 / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | (245.585,132 + 84.000) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,28 lần [simulated]** hoá đơn chia số yêu cầu: (4.373.585,132 / 978) / (329.585,132 / 1.200).
- Khoản lớn nhất là **làm lại: 51,77% [simulated]** = 2.264.000 / 4.373.585,132 × 100.

### Phép kiểm số để Cường tự kiểm chứng

- Đếm đủ **1.200 yêu cầu**, **1.624 lần chạy**; kết quả gồm 978 thành công + 74 làm lại + 148 chuyển nhân viên = 1.200.
- Tử số cộng cả 1.624 lần chạy, gồm lần lỗi; mẫu số CPS chỉ là 978 việc thành công. Không dùng 1.200 để tính CPS.
- Theo công thức chi phí cả hệ thống của lab: [4.373.585,132 + (74 + 148) × 12.000] / 1.200 = **5.864,65 đ/yêu cầu = 0,489× [simulated]** so với tự làm.
- Công thức hệ thống trên cộng 12.000 đ cho cả 222 yêu cầu không thành công theo quy ước B3; đây là giả định tính của lab, không phải khoản chi đã đo thêm từ CSV. A2 chưa gồm chi phí cố định.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công [simulated] | CPS / 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 783 / 824 = 95,02% | 916 / 824 = 1,112 | 2.695,64 đ | 0,225× |
| hang_nang | 158 | 117 / 158 = 74,05% | 232 / 158 = 1,468 | 8.220,73 đ | 0,685× |
| quoc_te | 150 | 41 / 150 = 27,33% | 348 / 150 = 2,320 | 22.515,17 đ | 1,876× |
| doi_tac | 68 | 37 / 68 = 54,41% | 128 / 68 = 1,882 | 10.214,87 đ | 0,851× |

- `quoc_te` không đáng đưa vào pilot: CPS **22.515,17 đ = 1,876× [simulated]**, thành công 27,33%; tỷ lệ `ok` theo lần 1–3 là 30,00% → 11,43% → 2,15%, nên chạy lại giúp ít và vẫn tốn chi phí.
- Đề xuất chỉ pilot `noi_dia + hang_nang`; tạm loại `doi_tac` vì CPS đã là **0,851× [simulated]** trước cố định và có điều khoản riêng cần kiểm soát.

### Đầu vào để kiểm tra lại A3

Lọc yêu cầu theo `loai`, rồi lấy mọi run có `request_id` thuộc tập đó. Tổng chi phí = token + tool + 2.000 × (phút xem lại + phút làm lại); CPS = tổng / thành công.

| Loại | Token + tool (đ) | Phút xem lại [simulated] | Phút làm lại [simulated] | Tổng chi phí (đ) [simulated] |
| --- | ---: | ---: | ---: | ---: |
| noi_dia | 178.687,298 | 471 | 495 | 2.110.687,298 |
| hang_nang | 45.825,976 | 173 | 285 | 961.825,976 |
| quoc_te | 79.121,766 | 145 | 277 | 923.121,766 |
| doi_tac | 25.950,092 | 101 | 75 | 377.950,092 |

Với `quoc_te`, số run `ok` / số run theo lần thử là **45/150, 12/105, 2/93**. `status == 'ok'` của run không đồng nghĩa yêu cầu cuối cùng `thanh_cong`; các tỷ lệ này mang tính mô tả, chưa chứng minh tác động nhân quả của chạy lại.

Cột CPS / 12.000 là tỷ số theo mẫu A3, có mẫu số khác chi phí tự làm mỗi yêu cầu. Kiểm tra công bằng theo công thức cả hệ thống của lab cho bốn loại lần lượt là **3.158,60; 9.201,43; 14.874,15; 11.028,68 đ/yêu cầu [simulated]**, chưa gồm cố định.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng toàn công ty | Việc thành công trong phạm vi mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định [simulated] | CPS có cố định / 12.000 đ [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185,19 đ | 4.599,09 đ | 0,383× |
| Một nửa: 22.500 yêu cầu/tháng | 16.875 | 2.370,37 đ | 5.784,27 đ | 0,482× |

- Chi phí cố định **không đổi kết luận về CPS tại 45.000 và 22.500 yêu cầu/tháng**: CPS có cố định đều dưới 12.000 đ, lần lượt **4.599,09 và 5.784,27 đ [simulated]**; khối lượng giảm một nửa làm phần cố định/việc tăng gấp đôi.

### Cách tính A4 và giới hạn so sánh

- Phạm vi có **982 yêu cầu, 900 thành công**, tổng chi phí **3.072.513,274 đ [simulated]**; CPS biến đổi = 3.072.513,274 / 900 = **3.413,90 đ [simulated]**.
- Giả định giữ cơ cấu và tỷ lệ thành công của mẫu: 45.000 × (982/1.200) = **36.825 yêu cầu thuộc phạm vi/tháng**; thành công = 45.000 × (900/1.200) = **33.750**. Không lấy 45.000 × 900/982.
- Phân bổ toàn bộ cố định cho phạm vi: 40.000.000 / 33.750 = **1.185,19 đ/việc**; cộng CPS biến đổi được **4.599,09 đ/việc [simulated]**.
- Ở 22.500 yêu cầu toàn công ty/tháng: thành công còn **16.875**, cố định = 40.000.000 / 16.875 = **2.370,37 đ/việc**; CPS có cố định = **5.784,27 đ [simulated]**.
- Kiểm tra cùng mẫu số mỗi yêu cầu trong phạm vi: [(3.072.513,274 + 82 × 12.000) / 982] + 40.000.000 / 36.825 = **5.217,09 đ/yêu cầu [simulated]**; nửa khối lượng là **6.303,31 đ/yêu cầu [simulated]**.

### Kết quả đối chiếu CP1 với code của Vỹ

Ngày kiểm tra: **25/11/2026**; mã nguồn: `src/lab13.py` tại **`9f76372`**, chứa CP1 từ PR #1 (`c0be8ea`). Lệnh `cd src` rồi `python lab13.py` kết thúc với exit code **0**, ba phép thử A1 đạt. Phần CP2 và E1 cũng được chạy do có sẵn trong chương trình; bảng B chưa được hoàn thiện trong phạm vi CP1 này.

| Hạng mục | Kiểm số độc lập | Code Vỹ / output | Kết luận |
| --- | --- | --- | --- |
| A1 | 1,20 · 1,25 · 1,25 | 1,20 · 1,25 · 1,25; ba assert đạt | Khớp |
| A2: token, tool, chạy lại | 245.585,132; 84.000; 93.804,488 đ | Giá trị hàm khớp; output làm tròn 245.585; 84.000; 93.804 đ | Khớp |
| A2: xem lại, làm lại [simulated] | 1.780.000; 2.264.000 đ | 1.780.000; 2.264.000 đ | Khớp |
| A2: tổng và thành công | 4.373.585,132 đ [simulated]; 978 yêu cầu | Output 4.373.585 đ [simulated]; 978 yêu cầu | Khớp |
| A2: CPS; hệ thống/yêu cầu [simulated] | 4.471,97; 5.864,65 đ | Output 4.472; 5.865 đ | Khớp sau làm tròn |
| A3: CPS theo thứ tự bốn loại [simulated] | 2.695,64; 8.220,73; 22.515,17; 10.214,87 đ | Output 2.696; 8.221; 22.515; 10.215 đ | Khớp sau làm tròn |
| A4: thành công/tháng ở hai quy mô | 33.750; 16.875 | 33.750; 16.875 | Khớp |
| A4: CPS có cố định [simulated] | 4.599,09; 5.784,27 đ | Output 4.599; 5.784 đ | Khớp sau làm tròn |

Phương pháp kiểm chéo: đọc lại CSV bằng `csv.DictReader`, tính tiền bằng `decimal.Decimal` với giá đề bài, độc lập với `mo_hinh`; sau đó so giá trị chưa làm tròn với hàm của Vỹ. Tổng cộng **83 phép so đạt**: 6 tập dữ liệu (toàn mẫu, 4 loại, phạm vi pilot) × (12 trường kết quả + số lần chạy trung bình), 2 mức CPS có cố định A4 và 3 giá trị A1.

Ngưỡng kiểm tra số thực: `math.isclose(rel_tol=1e-12, abs_tol=1e-8)`; kết quả khớp tới độ chính xác số thực, nằm trong mức sai số rubric **2%**. Riêng A3, tỷ lệ thành công suy ra từ số thành công/số yêu cầu; bảng `status == 'ok'` của quốc tế cũng khớp 30,0% · 11,4% · 2,2% trên output. A4 đã kiểm tra cách chia theo tổng mẫu 1.200, đúng giả định quy mô toàn công ty.

**Kết luận công cụ:** Không phát hiện chênh lệch CP1 cần sửa code hoặc số trong bảng. Đây là kiểm chứng có AI hỗ trợ, chưa phải bằng chứng Cường đã tự tính tay; Cường cần tự kiểm tra ít nhất một phép tính trước khi xác nhận báo cáo cá nhân.

## B1 · Đổi từng yếu tố

Mốc gốc: **4.471,9684376 đ/việc thành công [simulated]** (A2). Tỷ lệ thay đổi = (CPS kịch bản / CPS gốc − 1) × 100; mọi kịch bản chưa gồm cố định. Các hệ số xem lại/làm lại chỉ thay khoản chi tương ứng, không đổi số thành công, trừ hai kịch bản giới hạn lần chạy.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (đ) [simulated] | Thay đổi (%) [simulated] |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723,08 | +5,62% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346,41 | −2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292,01 | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.561,95 | −20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.786,90 | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.314,50 | −25,88% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.505,71 | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Bỏ run `attempt > 2`; yêu cầu vượt giới hạn chuyển nhân viên, phút xem lại và làm lại bằng 0 | 4.237,29 | −5,25% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.110,99 | −8,07% |

Phép kiểm tay ví dụ: xem lại gấp đôi → (4.373.585,132 + 1.780.000) / 978 = **6.292,01 đ [simulated]**. Giảm nửa khoản xem lại → (4.373.585,132 − 890.000) / 978 = **3.561,95 đ [simulated]**; độ giảm bằng nửa độ tăng khi giữ số chưa làm tròn.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: (4.373.585,132 + 245.585,132 + 1.780.000) / 978 = **6.543,12 đ, tăng 46,31% [simulated]**; tác động bằng tổng riêng 5,61519% + 40,69888% do mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố theo mức tăng trong B1: **1. Số ca làm lại (+51,77%); 2. Tỉ lệ xem lại (+40,70%); 3. Lương nhân viên (+23,12%) [simulated]**. Lương chỉ tăng 25% trong khi hai yếu tố đầu gấp đôi; đây là xếp hạng các kịch bản đề cho.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng trợ lý + 12.000 × số yêu cầu không thành công, theo quy ước lab. CPS = tổng trợ lý / số thành công; hai mục tiêu tối ưu khác nhau. Kịch bản giới hạn chạy lại là giả định tính từ dữ liệu, không phải thử nghiệm đã triển khai.

| Giới hạn | Tổng chi phí trợ lý (đ) [simulated] | Số yêu cầu không thành công | Chi phí cả hệ thống (đ) [simulated] | Chi phí mỗi việc thành công (đ) [simulated] |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.780,64 | 319 | 7.449.780,64 | 4.110,99 |
| 2 lần | 4.093.220,23 | 234 | 6.901.220,23 | 4.237,29 |
| 3 lần | 4.373.585,13 | 222 | 7.037.585,13 | 4.471,97 |

- **2 lần** rẻ nhất cho công ty: **6.901.220,23 đ [simulated]**; CPS thấp nhất ở **1 lần: 4.110,99 đ [simulated]**. Chọn 1 lần đẩy thêm **85 yêu cầu** sang nhân viên và tăng tổng hệ thống **548.560,41 đ [simulated]** so với 2 lần.

Phép kiểm tay: 2 lần có 966 thành công, 234 không thành công; 4.093.220,230 + 234 × 12.000 = **6.901.220,230 đ [simulated]**. Tương tự, số thành công ở 1 và 3 lần là **881 và 978**; tổng thành công + không thành công luôn bằng 1.200.

## B4 · Nếu phải xem lại tất cả

- Xem lại 100% với 9 phút làm lại/ca: **11.742,79 đ = 0,979×**; với trung bình dữ liệu 15,2973 phút/ca: **12.414,50 đ = 1,035× [simulated]** so với 12.000 đ, chưa gồm cố định và phần nhân viên làm thay.
- Pilot phải học cách giảm tỉ lệ xem lại an toàn và đo phút thực tế: với xem lại 100%, mức hòa vốn CPS là **5,122 phút/lần** (làm lại 9 phút) hoặc **4,803 phút/lần [simulated]** (trung bình dữ liệu).

### Đầu vào và cách tự kiểm B4

- Phạm vi có **982 yêu cầu**, **948 yêu cầu có ít nhất một run `ok`**, **48 ca `lam_lai`**, **900 thành công**. Xem lại 100% ở đây áp dụng cho 948 yêu cầu có kết quả `ok`, không phải mọi lần chạy.
- Token + tool của mọi run trong phạm vi = **224.513,274 đ**; xem lại = 948 × 5 × 2.000 = **9.480.000 đ [simulated]**.
- Với 9 phút/ca: làm lại = 48 × 9 × 2.000 = **864.000 đ [simulated]**; tổng = **10.568.513,274 đ [simulated]**; chia 900 được **11.742,79 đ [simulated]**.
- Trung bình từ toàn bộ 74 ca làm lại = 1.132 / 74 = **15,297297… phút/ca [simulated]** (hiển thị 15,3); dùng số chưa làm tròn cho 48 ca trong phạm vi: tổng = **11.173.053,81454 đ [simulated]**, chia 900 = **12.414,50 đ [simulated]**.
- Nếu chủ động làm tròn giả định lên 15,3 phút: tổng = **11.173.313,274 đ**, CPS = **12.414,79 đ [simulated]**. Code Vỹ giữ trung bình chưa làm tròn, nên output **12.415 đ [simulated]** là đúng; số 12.414 đ trong hướng dẫn lệch dưới 0,01%, trong ngưỡng rubric 2%.
- Ngưỡng phút xem lại = (12.000 × 900 − 224.513,274 − tiền làm lại) / (948 × 2.000). Đây là hòa vốn theo CPS biến đổi của bài B4, chưa phải hòa vốn toàn bộ chi phí công ty.

### Bằng chứng đối chiếu CP2

Ngày **25/11/2026**, nền **`e3be9e9`**, code CP2 từ PR #2 (`f18aa18`). Tính độc lập bằng `csv.DictReader` và `decimal.Decimal`, sau đó so với `mo_hinh` của Vỹ: **55 phép so đạt** (11 cấu hình × 5 giá trị: tổng, thành công, không thành công, CPS, chi phí hệ thống), với `rel_tol=1e-12`, `abs_tol=1e-8`.

Thêm **4 kiểm tra tuyến tính đạt**: ba cặp gấp đôi/giảm nửa và một kịch bản ghép. B4 đối chiếu đầu vào, tổng, CPS và ngưỡng hòa vốn với output code; khác biệt hiển thị chỉ do làm tròn. Chạy `python lab13.py` trong `src/` hoàn tất, ba phép thử A1 và các assert tuyến tính B1–B2 đạt.

Kết quả có AI hỗ trợ, chưa xác nhận Cường đã tự kiểm tay; có thể dùng phép cộng B3 hoặc công thức B4 ở trên để tự kiểm chứng. CP2 này chỉ sửa bảng chi phí; không sửa code của Vỹ hoặc hai CSV.
