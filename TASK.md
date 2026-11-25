# Kế hoạch phân công nhiệm vụ theo Checkpoint — Lab 13 (NhomABC · L3B)

> **Repo nhóm:** `https://github.com/Do-Hong-Vy/K5-L3B-DAY13-NhomABC-LaunchEconomics`  
> **Mốc tại lớp:** 14:00–18:00 (hồ sơ sẵn sàng lúc **17:00** để duyệt chéo Gate 2a; chốt bản tại lớp lúc **17:45–18:00**)  
> **Deadline LMS:** **23:59 GMT+7** ngày lab — **cả 4 thành viên phải tự nộp link repo nhóm bằng tài khoản LMS cá nhân**.

---

## 1. Bảng phân vai & định danh nhánh

| STT | Thành viên | MSSV | GitHub | Vai trò chính (CP1–CP2) | Vai trò sau giải lao (CP3–CP5) | Tiền tố nhánh | File báo cáo cá nhân |
| --: | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Đỗ Hồng Vỹ** | `2A202604107` | `@Do-Hong-Vy` | Người viết code (`src/lab13.py`) | Review code CP4, viết code & hồ sơ E1–E2 (`chi_so.md`), QA chốt repo | `vy/...` | `report/team/2A202604107_DoHongVy.md` |
| 2 | **Phạm Hà Nam** | `2A202604023` | `@phamhanam` | Người gắn nhãn 1 (đọc đề, soát điều kiện "Xong khi") | Gắn nhãn độc lập #1 (CP3), soạn `pilot_plan.yaml` (CP4), ghi `phieu_cham.md` (CP5) | `nam/...` | `report/team/2A202604023_PhamHaNam.md` |
| 3 | **Nguyễn Trung Dũng** | `2A202604084` | `@bomgoa1102` | Người gắn nhãn 2, kiêm giữ hồ sơ (`ho_so_launch_v0.md`) | Gắn nhãn độc lập #2 & chốt `bang_loi.md` (CP3), chốt `ho_so_launch_v0.md` & `group_report.md` | `dung/...` | `report/team/2A202604084_NguyenTrungDung.md` |
| 4 | **Lê Khánh Cường** | `2A202603999` | `@lekhanhcuongvk1` | Người kiểm số (tính tay đối chiếu, điền `bang_chi_phi.md`) | **Đổi vai viết code** `TODO CP4` trong `src/lab13.py` & chạy kiểm chứng máy thứ 2, kiểm số toàn hồ sơ | `cuong/...` | `report/team/2A202603999_LeKhanhCuong.md` |

> **Lưu ý đổi vai sau giải lao (15:20–15:35):** Theo yêu cầu của lab (`TEAM.md`), sau giờ giải lao đổi người viết code giữa **Đỗ Hồng Vỹ** và **Lê Khánh Cường** để ít nhất 2 thành viên tự tay viết/chạy code tính chi phí và đảm bảo `src/lab13.py` chạy thông suốt trên ít nhất 2 máy khác nhau.

---

## 2. Quy ước Git Branch & Pull Request (Bắt buộc)

### 2.1. Quy trình 5 bước cho MỖI task
Không push trực tiếp lên `main`. Mọi thay đổi đều đi qua **nhánh riêng → Pull Request (PR) → Review → Merge vào `main`**:

```bash
# Bước 1: Luôn cập nhật nhánh main mới nhất trước khi làm task mới
git checkout main
git pull origin main

# Bước 2: Tạo nhánh riêng theo đúng tên quy ước của checkpoint
git checkout -b <tien-to>/<cp>-<mo-ta-ngan>

# Bước 3: Làm việc đúng file mình phụ trách và chạy lệnh tự kiểm tra
git status
git add <cac-file-da-sua>
git commit -m "feat(cp1): mo ta ngan gon viec da lam"

# Bước 4: Đẩy nhánh lên GitHub
git push -u origin <tien-to>/<cp>-<mo-ta-ngan>

# Bước 5: Mở Pull Request vào nhánh `main` trên GitHub
# - Ghi rõ: Checkpoint nào, đã chạy lệnh kiểm tra gì, số liệu đối chiếu (nếu có)
# - Gắn ít nhất 1 Reviewer theo bảng phân công bên dưới
# - Khi Reviewer duyệt (Approve) → Merge PR vào `main` (chọn Merge hoặc Squash and merge)
```

### 2.2. Nguyên tắc chống xung đột (File Ownership)
Mỗi file chỉ có **1 người chịu trách nhiệm chính ghi file tại mỗi checkpoint** để tránh merge conflict khi làm song song:

| File | Chủ sở hữu ghi (Owner) | Ghi chú tránh xung đột |
| --- | --- | --- |
| `src/lab13.py` | Vỹ (CP1, CP2, CP5-E1) → Cường (CP4) | Tuần tự theo CP; luôn `pull main` trước khi tách nhánh tiếp theo |
| `report/team/bang_chi_phi.md` | Cường (CP1, CP2) | Chỉ Cường sửa; Vỹ & Nam review trên PR |
| `report/team/bang_loi.md` | Nam (cột Nhãn người 1) → Dũng (cột Nhãn người 2 + chốt bảng 5 ca) | Nam merge PR nhãn 1 trước (khi Dũng đã tự ghi nhãn 2 độc lập), sau đó Dũng pull và chốt bản cuối |
| `report/team/pilot_plan.yaml` | Nam (CP4) | Dùng kết quả D1 từ PR `cuong/cp4-sample-size` đã merge |
| `report/team/chi_so.md` | Vỹ (CP5) | Cường kiểm số và Nam soát quy tắc trên PR |
| `report/team/ho_so_launch_v0.md` | Dũng (CP1 → CP5) | Chỉ Dũng cập nhật file này xuyên suốt buổi để không bị conflict |
| `report/team/phieu_cham.md` | Nam (CP5 — Duyệt chéo) | Cả nhóm cùng thảo luận, Nam ghi và tạo PR |
| `report/team/group_report.md` | Dũng (Đóng gói) | Tổng hợp sau khi duyệt chéo xong |
| `report/team/<MSSV>_<HoTen>.md` | Mỗi thành viên tự tạo file riêng | 4 file độc lập, tạo 4 PR song song, **0% xung đột** |
| `TEAM.md` | Vỹ tổng hợp cập nhật cuối (nhánh `vy/final-team-qa`) | Các thành viên gửi link PR/commit đóng góp để Vỹ cập nhật 1 lần cuối cùng |

### 2.3. Quy tắc cấm (áp dụng cho mọi PR)
- **KHÔNG** sửa `src/logix_runs.csv`, `src/logix_requests.csv`, `src/lab13_starter.py`, và file mẫu `report/team/MSSV_HoTen.md`.
- **KHÔNG** commit `.venv/`, `.env`, secret hay file tạm/file rác trong `report/team/`.
- **Mọi số liệu** tính từ `phut_xem_lai_simulated` và `phut_lam_lai_simulated` **bắt buộc có nhãn `simulated`**.
- **KHÔNG** dùng từ tiếng Anh chỉ môi trường chạy chính thức (quy tắc 5 trong `README.md`) trong bất kỳ file nào thuộc `report/team/`.
- **KHÔNG** ghi người phụ trách là `"cả đội"` — luôn ghi đúng **một vai trò cụ thể**.
- **Mỗi câu trả lời ngắn** trong bảng chi phí không quá 3 dòng và phải có ít nhất một con số.

---

## 3. Tổng quan tiến độ & lịch trình PR

| Giai đoạn | Khung giờ | PR / Commit đã merge vào `main` | Trạng thái thực tế |
| --- | --- | --- | --- |
| **CP0 · Khởi động** | 14:00–14:10 | `52b15a6` (`TEAM.md`, `task.md`) | **Hoàn tất** |
| **CP1 · Nhiệm vụ A** | 14:10–14:53 | PR #1 (`vy/cp1-cost-model`), PR #6 (`cuong/cp1-bang-chi-phi`) | **Hoàn tất** (3 phép thử A1 ĐẠT, 83 phép so khớp) |
| **CP2 · Nhiệm vụ B** | 14:53–15:20 | PR #2 (`vy/cp2-sensitivity`), PR #7 & #10 (`cuong/cp2-bang-chi-phi`) | **Hoàn tất** (9 kịch bản + tuyến tính ĐẠT) |
| **Giải lao · Đổi vai** | 15:20–15:35 | Cường nhận viết code CP4 & chạy kiểm chứng `src/lab13.py` | **Hoàn tất** |
| **CP3 · Nhiệm vụ C** | 15:35–16:08 | PR #5 (`nam/cp3-label-1`), PR #8 & #13 (`NTD`), PR #16 | **Chốt 20/20 nhãn thống nhất & 5 ca khắc phục** *(ghi nhận trung thực thiếu bộ nhãn độc lập #2)* |
| **CP4 · Nhiệm vụ D** | 16:08–16:36 | PR #9 (`cuong/cp4-sample-size`), `b084e1a` (`pilot_plan.yaml`), PR #17 & #19 | **Hoàn tất** (D1, D2, YAML sạch 0 `?`, 4 luật dừng 4 vế) |
| **CP5 · Nhiệm vụ E** | 16:36–17:00 | PR #3 (`vy/cp5-chi-so`), PR #8, #12, #13, #15–#17 (`ho_so_launch_v0.md`) | **Hoàn tất trước 17:00** (7 mục + **Go có điều kiện**) |
| **CP5 · Duyệt chéo** | 17:00–17:45 | PR #18 (`vy/cp5-phieu-cham`, Vỹ thực hiện thay Nam) | **Hoàn tất** (chấm Nhóm Rua 30/30; nhận 30/30 từ Nhóm Rua) |
| **Đóng gói & Nộp** | 17:45–18:00 | PR #4, #11, #13, #14 (4 báo cáo cá nhân), PR #19, PR #20 | **Hoàn tất trên GitHub** — chỉ còn 4 thành viên tự nộp link LMS |

---

## 4. Phân công chi tiết từng Checkpoint

### CP0 · Chuẩn bị & cài đặt môi trường (14:00–14:10)

- [x] **Cả 4 thành viên (`@Do-Hong-Vy`, `@phamhanam`, `@bomgoa1102`, `@lekhanhcuongvk1`)**:
  - Clone repo nhóm `K5-L3B-DAY13-NhomABC-LaunchEconomics` (không làm trên repo đề bài).
  - Trong thư mục `src/`, tạo môi trường ảo `.venv` và cài `requirements.txt` (thêm `pyyaml` nếu thiếu):
    ```powershell
    cd src
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt pyyaml
    python -c "import pandas, numpy, scipy, statsmodels, yaml; print('san sang')"
    ```
  - Kiểm tra email của Nam, Dũng, Cường để bổ sung vào `TEAM.md` ở bước chốt cuối (hoặc trong 1 PR nhỏ ngay đầu buổi).

---

### CP1 · Nhiệm vụ A — Mô hình chi phí mỗi việc thành công (14:10–14:53)

**Tài liệu đối chiếu:** `CHECKPOINTS.md` (CP1), `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (Nhiệm vụ A).

#### 1. Đỗ Hồng Vỹ (`@Do-Hong-Vy`) — Người viết code
- **Nhánh:** `vy/cp1-cost-model`
- **File sửa:** `src/lab13.py`
- **Reviewer PR:** `@lekhanhcuongvk1`, `@phamhanam`
- **Đầu việc:**
  - [x] Viết 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) tại `TODO CP1`.
  - [x] Chạy kiểm tra đạt `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25) trước khi viết tiếp.
  - [x] Viết hàm `mo_hinh(runs, reqs, ...)` cho A2 (lọc `runs` theo `request_id`, tính mọi lần chạy kể cả lỗi, chia cho `ket_qua == 'thanh_cong'`, giữ sẵn tham số `gia_vao`, `gia_ra`, `gia_tool`, `luong_phut`, `he_so_xem_lai`, `he_so_lam_lai`, `max_lan_chay` để CP2 gọi lại).
  - [x] Viết phần tính A3 (chạy `mo_hinh` theo từng `loai`: `noi_dia`, `hang_nang`, `quoc_te`, `doi_tac` và tính tỉ lệ `status == 'ok'` theo từng `attempt` 1, 2, 3 cho từng loại).
  - [x] Viết phần tính A4 (chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` ở quy mô 45.000 yc/tháng và một nửa khối lượng).
  - [x] Chạy `cd src && python lab13.py`, gửi output cho Cường đối chiếu, push nhánh và **tạo PR vào `main`**.

#### 2. Lê Khánh Cường (`@lekhanhcuongvk1`) — Người kiểm số
- **Nhánh:** `cuong/cp1-bang-chi-phi`
- **File sửa:** `report/team/bang_chi_phi.md`
- **Reviewer PR:** `@Do-Hong-Vy`, `@phamhanam`
- **Đầu việc:**
  - [x] Tính tay đối chiếu tối thiểu: 1 dòng trong A2 (ví dụ: xem lại, làm lại, `cps`), chi phí cả hệ thống khi so với 12.000 đ (cộng phần nhân viên làm thay 222 ca không thành công → 5.865 đ/yc = 0,49×), và phép chia chi phí cố định A4 (1.185 đ/việc ở 45.000 yc/tháng; 2.370 đ/việc ở nửa khối lượng).
  - [x] Đối chiếu số từ `src/lab13.py` với công thức và slide chữa lúc 14:50 (đảm bảo sai số ≤ 2%).
  - [x] Điền đầy đủ các mục **A1, A2 (đủ 9 dòng), A3 (đủ 4 loại), A4** và các câu trả lời ngắn (≤ 3 dòng, có số, ghi đủ nhãn `simulated`) vào `report/team/bang_chi_phi.md`.
  - [x] Push nhánh và **tạo PR vào `main`**.

#### 3. Phạm Hà Nam (`@phamhanam`) — Người gắn nhãn 1 (QA & theo dõi "Xong khi")
- **Nhánh:** *(Không tạo nhánh code ở CP1; review PR trên GitHub)*
- **Đầu việc:**
  - [x] Đọc đề CP1, nhắc nhóm không mắc các lỗi phổ biến (quên `keep_default_na=False`, quên chia 1.000 cho token, chia mẫu cho 1.200 thay vì 978, so sánh 4.472 đ với 12.000 đ mà quên ca `chuyen_nhan_vien`).
  - [x] Review & duyệt 2 PR `vy/cp1-cost-model` và `cuong/cp1-bang-chi-phi` theo tiêu chí "Xong khi": đủ 3 phép thử ĐẠT, đủ 9 dòng A2 có nhãn `simulated`, đủ 4 dòng A3, trả lời rõ vì sao `quoc_te` không đáng chạy và chạy lại 3 lần không giúp.
  - [x] Đọc trước định nghĩa 5 loại lỗi Google PAIR trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` để chuẩn bị cho CP3 (**chưa thảo luận 20 ca lỗi với Dũng**).

#### 4. Nguyễn Trung Dũng (`@bomgoa1102`) — Người gắn nhãn 2, kiêm giữ hồ sơ
- **Nhánh:** `dung/cp1-ho-so-init`
- **File sửa:** `report/team/ho_so_launch_v0.md`
- **Reviewer PR:** `@lekhanhcuongvk1`
- **Đầu việc:**
  - [x] Điền dòng đầu `Nhóm: NhomABC · Lớp: L3B` trong `report/team/ho_so_launch_v0.md`.
  - [x] Sau khi Cường chốt số CP1, điền **Mục 1 (Chi phí mỗi việc thành công)** (ghi rõ cả tổng thể, trong phạm vi `noi_dia + hang_nang` đã cộng cố định, nhãn `simulated`) và **Mục 3 (So với nhân viên tự làm)** (ghi rõ so sánh công bằng cả hệ thống 0,49× và phạm vi pilot 0,38×–0,48×).
  - [x] Đặt cột Trạng thái = `Giả lập`, Người phụ trách = một vai trò cụ thể (ví dụ: `PM trợ lý hoàn phí` / `Giám đốc vận hành`).
  - [x] Push nhánh và **tạo PR vào `main`**.

---

### CP2 · Nhiệm vụ B — Bảng độ nhạy (14:53–15:20)

**Tài liệu đối chiếu:** `CHECKPOINTS.md` (CP2), `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (Nhiệm vụ B).

#### 1. Đỗ Hồng Vỹ (`@Do-Hong-Vy`) — Người viết code
- **Nhánh:** `vy/cp2-sensitivity` *(tách từ `main` sau khi CP1 đã merge)*
- **File sửa:** `src/lab13.py`
- **Reviewer PR:** `@lekhanhcuongvk1`, `@phamhanam`
- **Đầu việc:**
  - [x] Viết code tại `TODO CP2` trong `src/lab13.py`:
    - **B1:** Gọi `mo_hinh` cho đủ 9 kịch bản đổi từng yếu tố và in chi phí + `% thay đổi` so với A2.
    - **B2:** Tính kịch bản ghép (giá token ×2 đồng thời xem lại ×2).
    - **B3:** Tính chi phí cả hệ thống = `tổng trợ lý + 12.000 × số yêu cầu không thành công` cho 3 mức giới hạn: 1, 2, 3 lần chạy.
    - **B4:** Lọc `noi_dia + hang_nang`, tính kịch bản xem lại 100% (5 phút/yc có ít nhất 1 lần `ok`) theo cả 2 mức phút làm lại: **9 phút/ca** (đề cho) và **15,3 phút/ca** (trung bình thực tế cột `phut_lam_lai_simulated`), cùng mức hòa vốn phút xem lại.
  - [x] Tự kiểm tra: mọi kịch bản "giảm một nửa" có mức giảm đúng bằng 1/2 mức tăng của kịch bản "gấp đôi" tương ứng.
  - [x] Push nhánh và **tạo PR vào `main`**.

#### 2. Lê Khánh Cường (`@lekhanhcuongvk1`) — Người kiểm số
- **Nhánh:** `cuong/cp2-bang-chi-phi` *(tách từ `main` sau khi CP1 đã merge)*
- **File sửa:** `report/team/bang_chi_phi.md`
- **Reviewer PR:** `@Do-Hong-Vy`, `@phamhanam`
- **Đầu việc:**
  - [x] Kiểm tra tay tính cộng tuyến tính B1–B2 (tác động cặp = tổng hai tác động riêng) và kiểm tra phép cộng B3, B4.
  - [x] Điền đầy đủ **B1 (9 dòng), B2 (kết quả cặp + xếp hạng 3 yếu tố mạnh nhất), B3 (bảng 3 mức + câu trả lời ≤ 3 dòng), B4 (cả 2 con số 9 phút & 15,3 phút + bài học cho pilot, ≤ 3 dòng)** vào `report/team/bang_chi_phi.md`.
  - [x] Đối chiếu ngay với slide chữa lúc 15:18, đảm bảo có đủ nhãn `simulated`.
  - [x] Push nhánh và **tạo PR vào `main`**.

#### 3. Phạm Hà Nam (`@phamhanam`) — Người gắn nhãn 1 (QA)
- **Đầu việc:**
  - [x] Review PR `vy/cp2-sensitivity` và `cuong/cp2-bang-chi-phi` theo điều kiện "Xong khi" CP2: đủ 9 dòng B1, đúng thứ tự top 3 (1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên), B3 phân biệt rõ giới hạn rẻ nhất cho công ty (2 lần) vs CPS thấp nhất (1 lần), B4 có đủ 2 con số và nhãn `simulated`.

#### 4. Nguyễn Trung Dũng (`@bomgoa1102`) — Người gắn nhãn 2, kiêm giữ hồ sơ
- **Nhánh:** `dung/cp2-ho-so-update` *(tách từ `main` sau khi `dung/cp1-ho-so-init` đã merge)*
- **File sửa:** `report/team/ho_so_launch_v0.md`
- **Reviewer PR:** `@lekhanhcuongvk1`
- **Đầu việc:**
  - [x] Cập nhật **Mục 2 (Ba yếu tố nhạy nhất)** vào `report/team/ho_so_launch_v0.md` kèm % tác động từ B1–B2 và ghi chú B4 (trạng thái `Giả lập`, 1 vai trò phụ trách).
  - [x] Ghi nháp ý chính cho **Mục 7 (Rủi ro kinh tế)** dựa trên B1 & B4.
  - [x] Push nhánh và **tạo PR vào `main`**.

---

### Giải lao & Đổi vai người viết code (15:20–15:35)

- [x] **Lê Khánh Cường** pull `main` mới nhất, chạy `cd src && python lab13.py` trên máy của mình để xác nhận code A–B chạy hoàn chỉnh trên máy thứ hai và sẵn sàng nhận vai viết code cho CP4.
- [x] **Phạm Hà Nam** và **Nguyễn Trung Dũng** mở sẵn mục *"Hai mươi ca lỗi"* trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` — **tuyệt đối không trao đổi trước khi hết 8 phút gắn nhãn độc lập ở CP3**.

---

### CP3 · Nhiệm vụ C — Bảng lỗi và cách khắc phục (15:35–16:08)

**Tài liệu đối chiếu:** `CHECKPOINTS.md` (CP3), `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (20 ca lỗi), `RULES.md` (quy tắc gắn nhãn độc lập).

#### 1. Phạm Hà Nam (`@phamhanam`) — Người gắn nhãn 1
- **Nhánh:** `nam/cp3-label-1` *(tách từ `main`)*
- **File sửa:** `report/team/bang_loi.md`
- **Reviewer PR:** `@Do-Hong-Vy` *(chú ý: Dũng KHÔNG xem PR này trước khi chốt xong 20 nhãn của mình!)*
- **Đầu việc:**
  - [x] **Phút 0–8 (Độc lập):** Tự đọc 20 ca lỗi và phân loại theo 5 nhóm Google PAIR (nguyên nhân gốc: `Do người dùng`, `Hệ thống`, `Ngữ cảnh`, `Giới hạn hệ thống`, `Ngầm`).
  - [x] Điền tên `Người gắn nhãn 1: Phạm Hà Nam` và toàn bộ cột `Nhãn người 1` (ca 1–20) trong `report/team/bang_loi.md`.
  - [x] Commit, push nhánh `nam/cp3-label-1` và **tạo PR merge vào `main`** ngay khi Dũng báo đã hoàn tất 20 nhãn độc lập (lịch sử PR là bằng chứng gắn nhãn độc lập).
  - [x] **Phút 8–30:** Cùng Dũng so nhãn, tính tỉ lệ đồng thuận (mục tiêu ≥ 80%, tức ≥ 16/20; nếu < 80% phải viết lại định nghĩa), thống nhất nhãn & quy tắc phân biệt các ca lệch, cùng xây bảng khắc phục 5 ca và review PR hoàn thiện của Dũng.

#### 2. Nguyễn Trung Dũng (`@bomgoa1102`) — Người gắn nhãn 2, kiêm giữ hồ sơ
- **Nhánh:** `dung/cp3-bang-loi-ho-so` *(tách từ `main` NGAY SAU KHI PR `nam/cp3-label-1` đã merge)*
- **File sửa:** `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`
- **Reviewer PR:** `@phamhanam`, `@Do-Hong-Vy`
- **Đầu việc:**
  - [ ] **Phút 0–8 (Độc lập):** *(Ghi nhận thực tế: Dũng đã xem tài liệu hướng dẫn trước khi gắn độc lập nên nhóm giữ trung thực để cột `Nhãn người 2` = `Chờ`, không bịa nhãn theo `RULES.md` và đưa thành Điều kiện #2 trước bước `0.25`.)*
  - [x] Chốt cột `Nhãn thống nhất` (20/20 ca), quy tắc phân biệt nguyên nhân gốc và **Bảng khắc phục cho 5 ca (đủ 5 loại)** gắn `trace_id` khớp `chi_so.md` trong `report/team/bang_loi.md`.
  - [x] Cập nhật **Mục 5 (Bảng lỗi và cách khắc phục)** vào `report/team/ho_so_launch_v0.md` (trạng thái trung thực `Chưa`, 1 vai trò phụ trách `Kỹ sư trưởng agent`).
  - [x] Push nhánh và **tạo PR vào `main`**.

#### 3. Đỗ Hồng Vỹ (`@Do-Hong-Vy`) & Lê Khánh Cường (`@lekhanhcuongvk1`) — Hỗ trợ song song & QA
- **Nhánh (nếu cần sửa lỗi CP1–CP2):** `cuong/cp3-fix-ab` hoặc `vy/cp3-fix-ab`
- **Đầu việc:**
  - [x] Trong 8 phút đầu khi Nam & Dũng gắn nhãn độc lập: rà soát, hoàn thiện các điểm còn thiếu ở CP1–CP2 (nếu có chỉnh sửa sau slide chữa) và mở PR cập nhật.
  - [x] Sau khi Nam & Dũng so nhãn xong: góp ý kỹ thuật cho bảng khắc phục 5 ca (đặc biệt cột `Phát hiện bằng gì`: tên event, `trace_id`, ngưỡng, tần suất; đảm bảo khớp với thiết kế event ở E1).
  - [x] Review PR `nam/cp3-label-1` (Vỹ) và `dung/cp3-bang-loi-ho-so` (Vỹ + Nam).

---

### CP4 · Nhiệm vụ D — Kế hoạch Pilot (`pilot_plan.yaml`) (16:08–16:36)

**Tài liệu đối chiếu:** `CHECKPOINTS.md` (CP4), `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (Nhiệm vụ D).

#### 1. Lê Khánh Cường (`@lekhanhcuongvk1`) — Đổi vai viết code CP4 & Kiểm số
- **Nhánh:** `cuong/cp4-sample-size` *(tách từ `main`)*
- **File sửa:** `src/lab13.py`
- **Reviewer PR:** `@Do-Hong-Vy`, `@phamhanam`
- **Đầu việc:**
  - [x] Viết code tại `TODO CP4` trong `src/lab13.py`:
    - Hàm tính cỡ mẫu hai tỉ lệ (`NormalDist` / `statsmodels.stats.power.NormalIndPower`).
    - Tính đủ **5 câu D1**: (a) theo yêu cầu (`1.251`), (b) theo nhân viên `m = 75` (`DE = 2,48`, `3.103`/nhóm → cần 84 > 40 người), (c) 20 nhân viên/nhóm (tối đa `1.000`), (d) 6 depot/nhóm (tối đa `300`), (e) mức chênh 6 điểm (`859`/nhóm → `m ≥ 299`, `DE = 6,96`) và power thực tế ở mức chênh 5 điểm (`≈ 0,64`).
    - Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (toàn bộ `4,25%`; phạm vi `noi_dia + hang_nang` là `3,97%`) để làm cơ sở đặt luật an toàn.
  - [x] Chạy `cd src && python lab13.py`, xác nhận chạy sạch từ đầu đến cuối (A + B + D1).
  - [x] Push nhánh và **tạo PR vào `main`**.

#### 2. Phạm Hà Nam (`@phamhanam`) — Người gắn nhãn 1 (Phụ trách `pilot_plan.yaml`)
- **Nhánh:** `nam/cp4-pilot-plan` *(tách từ `main` sau khi Cường chốt kết quả D1)*
- **File sửa:** `report/team/pilot_plan.yaml`
- **Reviewer PR:** `@lekhanhcuongvk1`, `@Do-Hong-Vy`
- **Đầu việc:**
  - [x] Điền đầy đủ phần chú thích đầu file `report/team/pilot_plan.yaml`: kết quả 5 câu **D1**, 5 câu kiểm tra **D2** ("tách được tác động"), **đánh đổi đã chấp nhận** (chọn chia theo nhân viên 20+20, MDE 6 điểm, nêu rõ power 0,64 ở mức 5 điểm), và tỉ lệ `mo_lai_trong_7_ngay` hiện tại kèm lý do chọn ngưỡng.
  - [x] Điền toàn bộ trường YAML (`owner`, `scope` chỉ `noi_dia + hang_nang`, `assignment`, `rollout`, `primary_metric`, `identifiability`, `stop_rules`, `interim_looks`, `rollback`, `decision_date`, `simulated_inputs`).
  - [x] Viết ít nhất **3 luật dừng** (an toàn, chi phí, mức độ sử dụng) đủ 4 vế **`NẾU ... TRONG ... THÌ ... KHÔNG THÌ ...`**, có ngưỡng hợp lý so với baseline `4,25%`, thời hạn và người có quyền dừng.
  - [x] Xóa sạch mọi dấu `?` ngoài các dòng chú thích `#`, tự kiểm tra bằng lệnh:
    ```powershell
    cd src
    python -c "import yaml; d = yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8')); print('YAML OK:', list(d['pilot'].keys()))"
    Select-String -Path ..\report\team\pilot_plan.yaml -Pattern '^[^#]*\?'
    ```
  - [x] Push nhánh và **tạo PR vào `main`**.

#### 3. Đỗ Hồng Vỹ (`@Do-Hong-Vy`) — Kiểm số chéo & Review kỹ thuật
- **Đầu việc:**
  - [x] Đối chiếu công thức cỡ mẫu, design effect, `power = 0,64` trong PR `cuong/cp4-sample-size`.
  - [x] Review PR `nam/cp4-pilot-plan`: kiểm tra YAML hợp lệ, không còn `?`, các luật dừng không mâu thuẫn với số A–C, `simulated_inputs` liệt kê đủ các đầu vào giả lập, `owner` không ghi `"cả đội"`.

#### 4. Nguyễn Trung Dũng (`@bomgoa1102`) — Giữ hồ sơ
- **Nhánh:** `dung/cp4-ho-so-pilot` *(tách từ `main` sau khi PR `nam/cp4-pilot-plan` đã merge)*
- **File sửa:** `report/team/ho_so_launch_v0.md`
- **Reviewer PR:** `@phamhanam`
- **Đầu việc:**
  - [x] Cập nhật **Mục 6 (Pilot plan)** trong `report/team/ho_so_launch_v0.md` (cách chia 20+20 nhân viên, `m ≥ 299`, MDE 6 điểm, nêu thẳng power 0,64 ở mức 5 điểm, 3 luật dừng, trạng thái `Xong, có bằng chứng`, 1 vai trò phụ trách).
  - [x] Push nhánh và **tạo PR vào `main`**.

---

### CP5 · Nhiệm vụ E — Chỉ số, Rủi ro kinh tế & Hồ sơ Launch v0 (16:36–17:00)

> **Mốc cứng 17:00:** `report/team/ho_so_launch_v0.md` phải merge xong vào `main` để gửi cho nhóm hội đồng Gate 2a.

#### 1. Đỗ Hồng Vỹ (`@Do-Hong-Vy`) — Code E1 & File `chi_so.md`
- **Nhánh:** `vy/cp5-chi-so` *(tách từ `main` sau khi CP4 đã merge)*
- **File sửa:** `src/lab13.py`, `report/team/chi_so.md`
- **Reviewer PR:** `@lekhanhcuongvk1`, `@phamhanam`
- **Đầu việc:**
  - [x] Bổ sung phần tính thử 3 chỉ số E1 trong `src/lab13.py` (Chính: `82,83%`, Dùng: `27,12%`, An toàn: `4,25%`).
  - [x] Điền đầy đủ `report/team/chi_so.md`:
    - **Bảng E1:** 3 chỉ số tính thử (viết *"chỉ số trong đợt chạy thử là..."*, **KHÔNG** viết *"trợ lý đã nâng"*) + đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn (bắt lỗi ngầm).
    - **Danh sách event:** tối thiểu 6 event (khuyến nghị 8–10 event), mọi event đều có `trace_id`, ghi rõ Ai tạo / Thuộc tính chính / Thời điểm.
    - **Kiểm tra chéo:** ánh xạ từng chỉ số ở E1 dùng event nào để tính (bảo đảm không chỉ số nào bị thiếu event).
    - **Bảng E2 (Rủi ro kinh tế):** ít nhất 2–3 dòng (làm lại ×2, xem lại 100%, khối lượng thấp/chi phí cố định), số lấy trực tiếp từ `bang_chi_phi.md`, có nhãn `simulated`, dấu hiệu theo dõi, hành động và **1 vai trò phụ trách**.
  - [x] Push nhánh và **tạo PR vào `main` trước 16:50**.

#### 2. Nguyễn Trung Dũng (`@bomgoa1102`) — Chốt Hồ sơ Launch v0
- **Nhánh:** `dung/cp5-ho-so-v0` *(tách từ `main` ngay sau khi PR `vy/cp5-chi-so` merge)*
- **File sửa:** `report/team/ho_so_launch_v0.md`
- **Reviewer PR:** `@Do-Hong-Vy`, `@lekhanhcuongvk1`, `@phamhanam` *(cả nhóm thống nhất trước khi merge)*
- **Đầu việc:**
  - [x] Hoàn thiện **Mục 4 (Chỉ số chính, dùng, an toàn)** và **Mục 7 (Rủi ro kinh tế)** trong `report/team/ho_so_launch_v0.md`.
  - [x] Rà soát toàn bộ 7 mục gọn trong **1 trang**: mỗi mục có con số chính, Trạng thái đúng 1 trong 3 giá trị (`Xong, có bằng chứng` · `Chưa` · `Giả lập`, trong đó mục 1, 2, 3, 7 ghi `Giả lập`), Người phụ trách là 1 vai trò.
  - [x] Cùng cả nhóm chốt dòng cuối **Đề xuất** (`Go` / `Go có điều kiện` / `No-go`; nếu chọn `Go có điều kiện`, ghi rõ từng điều kiện, người phụ trách, ngày kiểm tra, và nêu thẳng mọi con số bất lợi như power 0,64 và xem lại 100% B4).
  - [x] Push nhánh và **tạo PR merge vào `main` trước 17:00**.

#### 3. Lê Khánh Cường (`@lekhanhcuongvk1`) & Phạm Hà Nam (`@phamhanam`) — Kiểm số & Soát luật trước 17:00
- **Đầu việc:**
  - [x] **Cường:** Đối chiếu chéo mọi con số giữa `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md`, xác nhận không có số mâu thuẫn.
  - [x] **Nam:** Soát đủ 5 quy tắc lab trên PR `vy/cp5-chi-so` và `dung/cp5-ho-so-v0` (nhãn `simulated`, không dùng từ cấm quy tắc 5, không có `"cả đội"`, không viết *"trợ lý đã nâng"*).

---

### CP5 · Duyệt chéo Gate 2a (17:00–17:45)

**Phân vai tại phiên hội đồng (cả 4 thành viên cùng tham gia):**
- **Gửi hồ sơ & trình bày 1 phút:** Nguyễn Trung Dũng (chính) + Đỗ Hồng Vỹ (hỗ trợ kỹ thuật).
- **Đọc & chấm hồ sơ nhóm `n + 1` (17:10–17:25):** Cả 4 thành viên chia tiêu chí soi lỗi — Cường kiểm số & nhãn `simulated`, Vỹ kiểm phạm vi & B4, Nam kiểm `pilot_plan` & luật dừng, Dũng tổng hợp quyết định hội đồng.
- **Công bố chấm 1 phút & đặt câu hỏi cho nhóm bạn:** Lê Khánh Cường / Phạm Hà Nam.
- **Trả lời hỏi đáp 1 phút (đội mình):** Cả 4 người nắm chắc 3 giải thích bắt buộc trong `RULES.md`:
  1. Vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công.
  2. Cách tính cỡ mẫu hiệu dụng khi chia theo cụm (giới hạn `c / ICC`) và đánh đổi MDE 6 điểm / power 0,64.
  3. Lý do của đề xuất cuối (gồm cả con số bất lợi B4 xem lại 100% và cách xử lý).

#### Ghi phiếu chấm hội đồng: Phạm Hà Nam (`@phamhanam`) *(Thực tế: Đỗ Hồng Vỹ hỗ trợ ghi & tạo PR thay — PR #18 `05cefb1`)*
- **Nhánh thực tế:** `vy/cp5-phieu-cham` *(đã merge vào `main` qua PR #18)*
- **File sửa:** `report/team/phieu_cham.md`
- **Reviewer PR:** `@bomgoa1102`, `@lekhanhcuongvk1`
- **Đầu việc:**
  - [x] Điền đủ tên nhóm chấm (`NhomABC`), nhóm được chấm, điểm từng tiêu chí (0 / 5 / 10) kèm **lý do có con số**, tổng điểm `/ 30`, quyết định hội đồng (`Go` / `Go có điều kiện` / `No-go`), lý do, câu hỏi đã đặt và câu trả lời của đội bạn ghi lại tại buổi.
  - [x] Push nhánh và **tạo PR vào `main`**.

---

### Đóng gói, Báo cáo nhóm, Báo cáo cá nhân & Nộp bài (17:45–18:00 · Deadline LMS 23:59)

#### 1. Báo cáo nhóm ngắn — Nguyễn Trung Dũng (`@bomgoa1102`)
- **Nhánh:** `dung/final-group-report` *(tách từ `main`)*
- **File sửa:** `report/team/group_report.md`
- **Reviewer PR:** `@Do-Hong-Vy`
- **Đầu việc:**
  - [x] Điền đủ 8 mục trong `report/team/group_report.md` (ngắn gọn ≤ 2 trang): thông tin nhóm (`NhomABC`, `L3B`), mục tiêu, tóm tắt giải pháp A–E kèm link tới 6 file hồ sơ, kết quả chính (đủ nhãn `simulated`) + kết quả duyệt chéo nhóm nhận được từ hội đồng, khó khăn & cách xử lý, dẫn sang `TEAM.md`, hạn chế & hướng cải thiện, tài liệu tham khảo.
  - [x] Push nhánh và **tạo PR vào `main`**.

#### 2. Báo cáo cá nhân (4 PR độc lập song song — KHÔNG xung đột)
Mỗi thành viên **copy** `report/team/MSSV_HoTen.md` (giữ nguyên file mẫu!), điền đủ 6 mục (đặc biệt **Mục 4 Bằng chứng** gồm link PR/commit và **Mục 5 Công cụ AI đã dùng & cách tự kiểm tra** theo `RULES.md`), rồi tạo PR vào `main`:

- [x] **Đỗ Hồng Vỹ (`@Do-Hong-Vy`)**: nhánh `vy/personal-report` → tạo `report/team/2A202604107_DoHongVy.md` → PR vào `main` (Reviewer: `@lekhanhcuongvk1`).
- [x] **Phạm Hà Nam (`@phamhanam`)**: nhánh `nam/personal-report` → tạo `report/team/2A202604023_PhamHaNam.md` → PR vào `main` (Reviewer: `@bomgoa1102`).
- [x] **Nguyễn Trung Dũng (`@bomgoa1102`)**: nhánh `dung/personal-report` → tạo `report/team/2A202604084_NguyenTrungDung.md` → PR vào `main` (Reviewer: `@phamhanam`).
- [x] **Lê Khánh Cường (`@lekhanhcuongvk1`)**: nhánh `cuong/personal-report` → tạo `report/team/2A202603999_LeKhanhCuong.md` → PR vào `main` (Reviewer: `@Do-Hong-Vy`).

#### 3. Chốt `TEAM.md` & QA cuối cùng — Đỗ Hồng Vỹ (`@Do-Hong-Vy`)
- **Nhánh:** `vy/final-team-qa` *(tách từ `main` sau khi tất cả PR trên đã merge)*
- **File sửa:** `TEAM.md`
- **Reviewer PR:** `@lekhanhcuongvk1`, `@phamhanam`, `@bomgoa1102`
- **Đầu việc:**
  - [x] Cập nhật đầy đủ **Email**, **Đóng góp cụ thể**, **Bằng chứng** (mã PR/commit) cho cả 4 thành viên trong `TEAM.md`.
  - [x] Chạy toàn bộ bộ lệnh QA bên dưới (Section 5) trước khi merge PR cuối vào `main`.
  - [x] Sau khi PR cuối merge, lấy mã commit chốt trên `main` (nếu cần cập nhật vào `TEAM.md` hoặc ghi nhận trong bản nộp) và xác nhận repo để chế độ **Public** (hoặc đã mời giảng viên).

---

## 5. Checklist QA cuối cùng trước khi nộp bài

Chạy các lệnh kiểm tra nhanh trên Windows PowerShell từ thư mục gốc repo (và `src/`):

```powershell
# 1. Chạy lại toàn bộ code từ đầu đến cuối trong src/
cd src
python lab13.py

# 2. Kiểm tra pilot_plan.yaml đọc được và không còn dấu ? ngoài dòng chú thích
python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8')); print('YAML OK')"
Select-String -Path ..\report\team\pilot_plan.yaml -Pattern '^[^#]*\?'

# 3. Kiểm tra không có từ cấm (quy tắc 5) trong toàn bộ thư mục report/team/
cd ..
Select-String -Path report\team\* -Pattern 'prod\x75ction'

# 4. Kiểm tra không sửa 2 file dữ liệu, lab13_starter.py và không commit .venv/.env
git status
git diff --name-only origin/main -- src/logix_runs.csv src/logix_requests.csv src/lab13_starter.py report/team/MSSV_HoTen.md
```

**Checklist bắt buộc (`SUBMISSION.md`):**
- [x] Tên repo đúng quy ước `K5-L3B-DAY13-NhomABC-LaunchEconomics`, repo Public hoặc đã mời giảng viên.
- [x] Mọi công việc đều đã được tạo PR từ nhánh riêng và merge sạch vào `main`.
- [x] `TEAM.md` đủ thông tin nhóm, thành viên, vai, đóng góp và bằng chứng.
- [x] Đủ 6 file hồ sơ trong `report/team/` đúng tên: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`.
- [x] Đủ `report/team/group_report.md` và **4 file báo cáo cá nhân** (giữ nguyên file mẫu `MSSV_HoTen.md`).
- [x] `cd src && python lab13.py` chạy hết trên **ít nhất 2 máy** trong nhóm (Vỹ & Cường), 3 phép thử A1 in **ĐẠT**.
- [x] Mọi con số từ cột `_simulated` đều ghi nhãn `simulated`.
- [x] `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn dấu `?` ngoài comment, có ≥ 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- [x] Mọi mục hồ sơ & bảng khắc phục có người phụ trách là **1 vai trò**, không ghi `"cả đội"`.
- [x] Đề xuất cuối trong `ho_so_launch_v0.md` là 1 trong 3: `Go` / `Go có điều kiện` / `No-go`.
- [x] Không có từ cấm (quy tắc 5) trong bất kỳ file hồ sơ nào.
- [x] Không commit `.venv/`, `.env`, API key hay password.
- [ ] **Cả 4 thành viên (`Vỹ`, `Nam`, `Dũng`, `Cường`) đã tự nộp link repo nhóm trên LMS trước 23:59 GMT+7.**
