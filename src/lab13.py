"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26                    # đồng cho 1.000 token đầu vào
GIA_RA = 130                    # đồng cho 1.000 token đầu ra
GIA_TOOL = 15                   # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000               # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000                # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000  # đồng / tháng
YEU_CAU_THANG_DAY_DU = 45_000       # yêu cầu / tháng ở quy mô đầy đủ
PHAM_VI_PILOT = ['noi_dia', 'hang_nang']


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')
    print(f'  - Tối đa 2 lần (p=0,8):           {so_lan_chay_ky_vong(0.8, 2):.2f} lần chạy')
    print(f'  - Chạy đến khi đúng (p=0,8):      {so_lan_chay_ky_vong(0.8):.2f} lần chạy')
    print(f'  - Hệ số CPS, tối đa 3 lần (p=0,8): {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f} lần')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong,
    khong_thanh_cong, cps, hoa_don_moi_yc, chi_phi_he_thong, chi_phi_he_thong_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    khong_thanh_cong = int(len(reqs) - thanh_cong)
    cps = tong / thanh_cong
    hoa_don_moi_yc = (tien_token.sum() + tien_tool.sum()) / len(reqs)
    chi_phi_he_thong = tong + khong_thanh_cong * BASELINE
    chi_phi_he_thong_moi_yc = chi_phi_he_thong / len(reqs)

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        khong_thanh_cong=khong_thanh_cong,
        cps=cps,
        hoa_don_moi_yc=hoa_don_moi_yc,
        chi_phi_he_thong=chi_phi_he_thong,
        chi_phi_he_thong_moi_yc=chi_phi_he_thong_moi_yc,
    )


def in_nhiem_vu_a(runs, reqs):
    """In kết quả Nhiệm vụ A2, A3 và A4 (CP1)."""
    print('\n========== A2 · MÔ HÌNH CHI PHÍ TỪ TRACE ==========')
    kq = mo_hinh(runs, reqs)
    tong_tool_calls = int(runs['tool_calls'].sum())
    phut_xem_lai = reqs['phut_xem_lai_simulated'].sum()
    phut_lam_lai = reqs['phut_lam_lai_simulated'].sum()
    print(f"Token (mọi lần chạy):                 {kq['token']:>12,.0f} đ  [đo từ trace]")
    print(f"Tool ({tong_tool_calls:,} lần gọi):               {kq['tool']:>12,.0f} đ  [đo từ trace]")
    print(f"  Trong đó, lần chạy thứ 2 và 3:      {kq['chay_lai']:>12,.0f} đ  [đo từ trace]")
    print(f"Xem lại ({phut_xem_lai:,.0f} phút):                  {kq['xem_lai']:>12,.0f} đ  [simulated]")
    print(f"Làm lại ({phut_lam_lai:,.0f} phút):                {kq['lam_lai']:>12,.0f} đ  [simulated]")
    print(f"Tổng chi phí:                         {kq['tong']:>12,.0f} đ  [có phần simulated]")
    print(f"Số việc thành công:                   {kq['thanh_cong']:>12,d} / {len(reqs):,d}")
    print(f"Chi phí mỗi việc thành công (CPS):    {kq['cps']:>12,.0f} đ  [simulated]")
    print(f"Hoá đơn token+tool / yêu cầu:         {kq['hoa_don_moi_yc']:>12,.1f} đ  [đo từ trace]")
    print(f"CPS / Hoá đơn mỗi yêu cầu:            {kq['cps'] / kq['hoa_don_moi_yc']:>12.1f}×  [simulated]")
    print(f"Tỉ trọng làm lại / tổng chi phí:      {kq['lam_lai'] / kq['tong'] * 100:>11.1f}%  [simulated]")
    print(f"Tỉ trọng xem lại / tổng chi phí:      {kq['xem_lai'] / kq['tong'] * 100:>11.1f}%  [simulated]")
    print(f"Tỉ trọng giờ nhân viên / tổng:        {(kq['xem_lai'] + kq['lam_lai']) / kq['tong'] * 100:>11.1f}%  [simulated]")
    print(f"Chi phí cả hệ thống / yêu cầu (so 12.000 đ): "
          f"{kq['chi_phi_he_thong_moi_yc']:,.0f} đ ({kq['chi_phi_he_thong_moi_yc'] / BASELINE:.2f}×)  [simulated]")

    print('\n========== A3 · TÁCH THEO LOẠI YÊU CẦU ==========')
    print(f"{'Loại':<12} {'Số YC':>6} {'TL TC':>8} {'Lần/YC':>8} {'CPS [sim]':>12} {'So 12.000đ':>11}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq_loai = mo_hinh(runs, sub)
        tl_tc = kq_loai['thanh_cong'] / len(sub) * 100
        lan_tb = sub['so_lan_chay'].mean()
        ty_le_baseline = kq_loai['cps'] / BASELINE
        print(f"{loai:<12} {len(sub):>6d} {tl_tc:>7.1f}% {lan_tb:>8.2f} {kq_loai['cps']:>10,.0f} đ {ty_le_baseline:>10.2f}×")

    print('\nTỉ lệ lần chạy status == ok theo loại và số lần thử (attempt):')
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(float)
    bang_ok = runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    bang_ok = bang_ok.reindex(['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'])
    for loai, row in bang_ok.iterrows():
        cols = '  '.join(f'Lần {int(a)}: {val:5.1f}%' if pd.notna(val) else f'Lần {int(a)}:   N/A'
                         for a, val in row.items())
        print(f'  {loai:<12} {cols}')

    print('\n========== A4 · CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang) ==========')
    reqs_pv = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    kq_pv = mo_hinh(runs, reqs_pv)
    ty_le_tc_mau = kq_pv['thanh_cong'] / len(reqs)
    print(f"CPS chưa gồm cố định (noi_dia + hang_nang): {kq_pv['cps']:,.0f} đ "
          f"({kq_pv['tong']:,.0f} đ / {kq_pv['thanh_cong']} việc)  [simulated]")
    for ten_kl, tong_yc_thang in [('45.000 yêu cầu/tháng', YEU_CAU_THANG_DAY_DU),
                                  ('Một nửa khối lượng (22.500)', YEU_CAU_THANG_DAY_DU // 2)]:
        viec_tc_thang = tong_yc_thang * ty_le_tc_mau
        co_dinh_moi_viec = CHI_PHI_CO_DINH_THANG / viec_tc_thang
        cps_co_dinh = kq_pv['cps'] + co_dinh_moi_viec
        print(f"  {ten_kl:<28} Việc TC/tháng: {viec_tc_thang:>8,.0f} | "
              f"Cố định/việc: {co_dinh_moi_viec:>6,.0f} đ | "
              f"CPS+cố định: {cps_co_dinh:>6,.0f} đ ({cps_co_dinh / BASELINE:.2f}×)  [simulated]")
    return kq


def in_nhiem_vu_b(runs, reqs):
    """In kết quả Nhiệm vụ B1, B2, B3 và B4 (CP2)."""
    print('\n========== B1 · BẢNG ĐỘ NHẠY (ĐỔI TỪNG YẾU TỐ) ==========')
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    ket_qua_b1 = {}
    print(f"{'Kịch bản':<28} {'CPS [sim]':>12} {'Thay đổi':>10}")
    print(f"{'Gốc (A2)':<28} {goc:>10,.0f} đ {'0.0%':>10}")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1) * 100
        ket_qua_b1[ten] = (cps, pct)
        print(f"{ten:<28} {cps:>10,.0f} đ {pct:>+9.1f}%")

    # Tự kiểm tra tuyến tính: giảm nửa = -1/2 × tăng gấp đôi
    for ten_tang, ten_giam in [
        ('Giá token gấp đôi', 'Giá token giảm một nửa'),
        ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm một nửa'),
        ('Số ca làm lại gấp đôi', 'Số ca làm lại giảm một nửa'),
    ]:
        tang = ket_qua_b1[ten_tang][0] - goc
        giam = goc - ket_qua_b1[ten_giam][0]
        assert abs(giam - 0.5 * tang) < 1e-6, f'Lỗi kiểm tra tuyến tính: {ten_tang}'
    print('Kiểm tra tuyến tính B1 (giảm một nửa = 1/2 mức tăng gấp đôi): ĐẠT')

    print('\n========== B2 · ĐỔI MỘT CẶP VÀ XẾP HẠNG ==========')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    pct_cap = (cps_cap / goc - 1) * 100
    tong_rieng = ket_qua_b1['Giá token gấp đôi'][1] + ket_qua_b1['Tỉ lệ xem lại gấp đôi'][1]
    assert abs(pct_cap - tong_rieng) < 1e-6, 'Mô hình cộng tuyến tính phải khớp tổng 2 tác động riêng'
    print(f"Giá token ×2 đồng thời xem lại ×2: {cps_cap:,.0f} đ ({pct_cap:+.1f}%, tổng riêng = {tong_rieng:+.1f}%)  [simulated]")
    print('Xếp hạng 3 yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%)')

    print('\n========== B3 · GIỚI HẠN CHẠY LẠI VÀ CHI PHÍ CẢ HỆ THỐNG ==========')
    print(f"{'Giới hạn':<10} {'Tổng trợ lý [sim]':>18} {'Không TC':>10} {'Cả hệ thống [sim]':>19} {'CPS [sim]':>12}")
    for max_k in (1, 2, 3):
        kq_k = mo_hinh(runs, reqs, max_lan_chay=max_k)
        print(f"{max_k} lần     {kq_k['tong']:>16,.0f} đ {kq_k['khong_thanh_cong']:>10d} "
              f"{kq_k['chi_phi_he_thong']:>17,.0f} đ {kq_k['cps']:>10,.0f} đ")

    print('\n========== B4 · XEM LẠI 100% (PHẠM VI noi_dia + hang_nang) ==========')
    reqs_pv = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    runs_pv = runs[runs['request_id'].isin(reqs_pv['request_id'])]
    so_yc_co_ok = int(runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique())
    so_ca_lam_lai = int((reqs_pv['ket_qua'] == 'lam_lai').sum())
    so_viec_tc = int((reqs_pv['ket_qua'] == 'thanh_cong').sum())
    tien_token_tool = (
        runs_pv['tokens_in'] / 1000 * GIA_VAO
        + runs_pv['tokens_out'] / 1000 * GIA_RA
        + runs_pv['tool_calls'] * GIA_TOOL
    ).sum()
    tien_xem_lai_100 = so_yc_co_ok * 5 * LUONG_PHUT

    lam_lai_all = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    phut_lam_lai_tb = float(lam_lai_all.mean())
    phut_lam_lai_tv = float(lam_lai_all.median())

    print(f"Phạm vi: {len(reqs_pv)} YC | Có ≥1 lần ok: {so_yc_co_ok} | Ca làm lại: {so_ca_lam_lai} | Thành công: {so_viec_tc}")
    print(f"Token+tool: {tien_token_tool:,.0f} đ | Xem lại 100% (5 phút/YC): {tien_xem_lai_100:,.0f} đ [simulated]")
    print(f"Phút làm lại thực tế trên toàn bộ ca lam_lai: TB = {phut_lam_lai_tb:.1f} phút, trung vị = {phut_lam_lai_tv:.1f} phút [simulated]")
    for nhan, phut_ll in [('Giả định đề (9,0 phút/ca)', 9.0),
                          (f'Trung bình dữ liệu ({phut_lam_lai_tb:.1f} phút/ca)', phut_lam_lai_tb)]:
        tien_ll = so_ca_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = tien_token_tool + tien_xem_lai_100 + tien_ll
        cps_b4 = tong_b4 / so_viec_tc
        hoa_von_phut = (BASELINE * so_viec_tc - tien_token_tool - tien_ll) / (so_yc_co_ok * LUONG_PHUT)
        print(f"  {nhan:<34} Tổng: {tong_b4:>10,.0f} đ | CPS: {cps_b4:>6,.0f} đ ({cps_b4 / BASELINE:.2f}×) | "
              f"Hoà vốn xem lại ≤ {hoa_von_phut:.1f} phút  [simulated]")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs)
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu (Lê Khánh Cường phụ trách).
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
    # TODO CP5 · Nhiệm vụ E1: tính thử 3 chỉ số trên 1.200 yêu cầu.
