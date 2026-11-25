# Team

## Thông tin nhóm

- Tên nhóm: NhomABC
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-NhomABC-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/Do-Hong-Vy/K5-L3B-DAY13-NhomABC-LaunchEconomics | Nhánh: `main` | Commit chốt: `HEAD` nhánh `main` (merge PR #20 `vy/sync-final-reports`)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đỗ Hồng Vỹ | 2A202604107 | 26ai.vydh@vinuni.edu.vn | Do-Hong-Vy | Người viết code |
|   2 | Phạm Hà Nam | 2A202604023 | hhnanaarg@gmail.com | phamhanam | Người gắn nhãn 1 |
|   3 | Nguyễn Trung Dũng | 2A202604084 | 26ai.dungnt9@vinuni.edu.vn | bomgoa1102 | Người gắn nhãn 2, kiêm giữ hồ sơ |
|   4 | Lê Khánh Cường | 2A202603999 | 26ai.cuonglk2@vinuni.edu.vn | lekhanhcuongvk1 | Người kiểm số |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## DoHongVy-2A202604107

### Phần việc phụ trách

- Người viết code (CP1–CP2): viết và chạy `src/lab13.py`; phụ trách E1–E2 (`report/team/chi_so.md`); lập kế hoạch `task.md`, review PR và QA toàn repo.

### Đóng góp cụ thể

- Thiết lập repo nhóm, cài môi trường `src/.venv`, lập kế hoạch chia việc theo checkpoint và luồng Git/PR (`task.md`).
- Cài đặt và kiểm chứng CP1 (A1–A4, 3 phép thử A1 ĐẠT) và CP2 (B1–B4, 4 kiểm tra tuyến tính ĐẠT) trong `src/lab13.py`.
- Bổ sung tính thử 3 chỉ số E1 trong `src/lab13.py` và hoàn thiện `report/team/chi_so.md` (5 chỉ số, 10 event có `trace_id`, ánh xạ kiểm tra chéo, 3 dòng rủi ro kinh tế).
- Review, đối chiếu và merge các PR của thành viên, tinh chỉnh đồng bộ hồ sơ trước phiên Gate 2a và tổng hợp QA.

### Bằng chứng

- PR #1 (`c0be8ea`), PR #2 (`f18aa18`), PR #3 (`50e0e1d`), PR #4 (`9f76372`), PR #15 (`ab4bbe2`), PR #16 (`28099ae`), PR #17 (`7f4dcfd`), PR #18 (`05cefb1`), PR #19 (`ba4e22e`), PR #20 (`vy/sync-final-reports`), commit `52b15a6`.
- File: `src/lab13.py`, `report/team/chi_so.md`, `report/team/phieu_cham.md`, `report/team/2A202604107_DoHongVy.md`, `task.md`, `TEAM.md`.

## PhamHaNam-2A202604023

### Phần việc phụ trách

- Người gắn nhãn 1: đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3; hoàn thiện `report/team/pilot_plan.yaml` ở CP4; phối hợp duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20/20 ca lỗi theo 5 loại Google PAIR dựa trên nguyên nhân gốc ở cột `Nhãn người 1` của `report/team/bang_loi.md`.
- Hoàn thiện `report/team/pilot_plan.yaml`: đủ 5 câu D1a–e, 5 câu D2, nêu rõ đánh đổi MDE 6 điểm / power `0,6417`, baseline mở lại 7 ngày (`4,25%` / `3,97%`) và các luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- Hoàn thiện báo cáo cá nhân `report/team/2A202604023_PhamHaNam.md` và tham gia duyệt chéo Gate 2a.

### Bằng chứng

- PR #5 (`e3be9e9`, commit `1a8cf91`), commit `b084e1a` (`pilot_plan.yaml`), PR #14 (`c945551`, báo cáo cá nhân).
- File: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/2A202604023_PhamHaNam.md`.

## NguyenTrungDung-2A202604084

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: điền `report/team/ho_so_launch_v0.md` xuyên suốt buổi; hoàn thiện bảng khắc phục 5 ca trong `report/team/bang_loi.md`; tổng hợp `report/team/group_report.md`.

### Đóng góp cụ thể

- Hoàn thiện bảng khắc phục 5 ca đủ 5 loại lỗi Google PAIR với ngưỡng đo được, khớp event `chi_so.md` và chốt cột `Nhãn thống nhất` trong `report/team/bang_loi.md`.
- Tổng hợp và hoàn thiện hồ sơ 1 trang 7 mục `report/team/ho_so_launch_v0.md` với đề xuất **Go có điều kiện**, nêu rõ số bất lợi (`power ≈ 0,64`, B4 xem lại 100%) và vai trò phụ trách cụ thể.
- Hoàn thiện báo cáo nhóm `report/team/group_report.md` (8 mục) và báo cáo cá nhân `report/team/2A202604084_NguyenTrungDung.md`.

### Bằng chứng

- PR #8 (`e0a7d19`), PR #12 (`bf624d6`), PR #13 (`3d51504`).
- File: `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `report/team/group_report.md`, `report/team/2A202604084_NguyenTrungDung.md`.

## LeKhanhCuong-2A202603999

### Phần việc phụ trách

- Người kiểm số (CP1–CP2): kiểm số độc lập và điền `report/team/bang_chi_phi.md`; đổi vai viết code CP4 (`TODO CP4`) trong `src/lab13.py`; rà soát số liệu hồ sơ nhóm.

### Đóng góp cụ thể

- Tính độc lập từ hai CSV bằng Python chuẩn (`csv`, `Decimal`), đối chiếu 83 phép so CP1 và 55 phép so + 4 kiểm tra tuyến tính CP2 khớp `src/lab13.py`, hoàn thiện trọn vẹn A1–A4 và B1–B4 trong `report/team/bang_chi_phi.md`.
- Đổi vai viết code CP4 (`co_mau_hai_ti_le`, `power_hai_ti_le`, `in_nhiem_vu_d`) trong `src/lab13.py`, chạy kiểm chứng toàn chương trình trên máy thứ hai và đối chiếu power (`0,6417`) bằng SciPy.
- Review số liệu và đóng góp nhận xét kỹ thuật cho `chi_so.md`, `pilot_plan.yaml`, `ho_so_launch_v0.md`; hoàn thiện báo cáo cá nhân `report/team/2A202603999_LeKhanhCuong.md`.

### Bằng chứng

- PR #6 (`91d67e3`), PR #7 (`70af75b`), PR #9 (`eef14af`), PR #10 (chỉnh lời văn), PR #11 (`5a72366`, báo cáo cá nhân).
- File: `report/team/bang_chi_phi.md`, `src/lab13.py`, `report/team/2A202603999_LeKhanhCuong.md`.
