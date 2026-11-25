# Phiếu chấm hội đồng Gate 2a

- Nhóm chấm (hội đồng): NhomABC (Lớp L3B)
- Nhóm được chấm: Nhóm Rua (Lớp L3B)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp số liệu (CPS 4.472 đ, cả hệ thống 5.865 đ = 0,49×, `simulated`); nêu thẳng các con số bất lợi (power 0,64 ở mức 5 điểm; xem lại 100% 11.743–12.415 đ = 0,98–1,03×, `simulated`; mở lại hiện tại 3,97%) kèm 4 điều kiện có vai trò và ngày kiểm tra cụ thể. Góp ý hoàn thiện: đồng bộ 10 event (Mục 4) vs 11 event (Điều kiện #3) và tách mốc duyệt kế hoạch 04/12 khỏi mốc đo phút thật 14/12. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi con số tính từ cột `_simulated` ở Mục 1, 2, 3, 7 và phần đề xuất đều có nhãn `simulated` và trạng thái `Giả lập`; thu hẹp phạm vi về `noi_dia + hang_nang` (4.599 đ = 0,38× gồm cố định 40 triệu/tháng; 0,48× ở nửa khối lượng) và loại `quoc_te` (22.515 đ = 1,88×), `doi_tac` (0,85×). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên 20 + 20 nhân viên phân tầng depot (đủ 20 cụm/nhóm), cỡ mẫu MDE 6 điểm rõ ràng (`m ≥ 299`, `DE = 6,96`, 859 hiệu dụng/nhóm), 4 luật dừng có ngưỡng/thời hạn/người dừng gắn baseline 3,97%; giải trình thuyết phục trong Q&A về chi phí biến đổi 8.000 đ không cộng 40 triệu cố định và cam kết chỉ bật lệch +2 điểm từ bước 25% (≥ 10 người). Góp ý ghi rõ 859 là mẫu hiệu dụng (5.980 mẫu thô). |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ của Nhóm Rua có bằng chứng số liệu chính xác, đủ nhãn `simulated`, hoàn thiện tốt 2 bộ nhãn lỗi độc lập (đồng thuận 19/20 = 95%), thiết kế pilot tách được tác động với 20 cụm/nhóm, công khai đánh đổi power 0,64 và rủi ro xem lại 100%, đồng thời trả lời phản biện thuyết phục về chi phí biến đổi 8.000 đ và cam kết sửa rõ ngưỡng +2 điểm áp dụng từ bước 25% (≥ 10 người) trước ngày bật pilot 07/12/2026.

**Một câu hỏi cho đội trình:** Ở bước rollout đầu mới mở cho 4 nhân viên (10%), luật dừng mở lại đối chứng +2 điểm (dễ báo động giả ~5,6%) và luật dừng chi phí (nếu cộng 40 triệu cố định sẽ lên ~15.300 đ/việc) được nhóm áp dụng thế nào để không dừng pilot oan ngay tuần đầu?

**Câu trả lời của đội trình (ghi lại tại buổi):** Luật chi phí không kích hoạt tuần đầu vì yêu cầu 2 tuần liên tiếp (bước 10% chỉ kéo dài 1 tuần) và ngưỡng 8.000 đ là chi phí biến đổi đo thật từ event (token, tool, phút xem lại và làm lại), không cộng 40 triệu cố định (khoản cố định thuộc quyết định mở rộng, không thuộc luật dừng nên mức ~15.300 đ không làm pilot dừng). Luật an toàn có 3 lớp chống báo động giả (vượt 3 ngày liên tiếp; trần tuyệt đối 6% so với baseline 3,97%; tạm tắt 30 phút để Kỹ sư trưởng agent rà trace trong 2 ngày rồi bật lại nếu là nhiễu, không huỷ pilot). Nhóm thừa nhận với 4 người mức lệch +2 điểm dễ báo động giả và cam kết ghi rõ bước 10% chỉ áp dụng trần tuyệt đối 6% + luật hoàn trùng, còn mức chênh +2 điểm so với đối chứng áp dụng từ bước 25% (≥ 10 người).
