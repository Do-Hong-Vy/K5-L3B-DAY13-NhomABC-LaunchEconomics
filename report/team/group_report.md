# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: NhomABC · Lớp: L3B
- Thành viên và vai trò: xem `TEAM.md`.

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá chi phí, lỗi và kế hoạch pilot của trợ lý hoàn phí LogiX-VN dựa trên mẫu 1.200 yêu cầu và 1.624 lần chạy. Chi phí có dùng thời gian nhân viên giả lập; kết quả chạy thử chưa có nhóm đối chứng.

## 3. Giải pháp

- A–B: tính chi phí và các kịch bản độ nhạy trong `bang_chi_phi.md`.
- C: phân loại ca lỗi và đề xuất cách khắc phục trong `bang_loi.md`; nhãn thống nhất còn chờ xác nhận.
- D: đề xuất pilot có đối chứng trong `pilot_plan.yaml`.
- E: đặc tả chỉ số và rủi ro trong `chi_so.md`, tổng hợp trong `ho_so_launch_v0.md`.

## 4. Kết quả

Chi phí mỗi việc thành công là 4.471,97 đ (`simulated`); chỉ số chính trong đợt chạy thử là 82,83% (994/1.200). Kế hoạch chọn 20 nhân viên mỗi nhóm, 5.980 yêu cầu thô mỗi nhóm và mức chênh 6 điểm; nếu tác động là 5 điểm thì power khoảng 0,64. Đề xuất là Go có điều kiện, theo hồ sơ launch.

Kết quả nhóm nhận được từ hội đồng Gate 2a: chưa có thông tin để ghi nhận.

## 5. Khó khăn và cách xử lý

Mẫu chỉ có 40 nhân viên, nên chia theo nhân viên không đủ power 0,80 để phát hiện chênh lệch 5 điểm. Kế hoạch chấp nhận mức 6 điểm và nêu rõ đánh đổi; nhóm cần rà soát ý nghĩa các vế “không thì” trong luật dừng trước pilot.

## 6. Tổng hợp đóng góp

Vai trò, phần việc và bằng chứng của từng thành viên được ghi trong `TEAM.md` và báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Thời gian xem lại và làm lại là `simulated`; cần đo thực tế trong pilot. Hai bộ nhãn lỗi độc lập và nhãn thống nhất chưa được xác nhận; cần hoàn thiện trước khi đánh giá CP3. Chạy thử chưa có đối chứng nên không kết luận tác động của trợ lý.

## 8. Tài liệu tham khảo

- Dữ liệu, công thức và hướng dẫn trong `docs/` của repo.
- Google PAIR, *People + AI Guidebook*, phần Errors + Graceful Failure: https://pair.withgoogle.com/guidebook/chapters/errors-failures/
