# Logic Toolkit

`logic-toolkit` là bộ cài đặt tích hợp ba toolkit độc lập:

1. `spec-driven-product-toolkit` — sản phẩm cần xây gì và workflow delivery.
2. `logic-toolkit` — behavior memory, invariant và logic pattern được giữ xuyên dự án/cuộc hội thoại.
3. `ops-toolkit` — repository/product có maintainable, attributable và handoff-ready không.

Nó cũng có một **reusable logic library** để tích lũy các invariant, state pattern và behavior pattern có thể dùng qua nhiều dự án.

Bộ cài đặt này là orchestration layer, không hợp nhất nội dung hoặc tạo checklist trùng lặp. Mỗi toolkit giữ ownership và thư mục state riêng.

## Cài đặt

```powershell
python logic_toolkit.py --target D:\path\to\your\app --profile balanced --check-only
python logic_toolkit.py --target D:\path\to\your\app --profile balanced
python logic_toolkit.py --target D:\path\to\your\app --profile balanced --ops-source D:\path\to\ops-toolkit
```

Profiles được chuyển tiếp cho spec toolkit: `prototype`, `balanced`, `production`.

Mặc định tool thứ ba được tìm ở thư mục sibling `ops-toolkit`. Dùng `--ops-source` nếu repo nằm ở nơi khác.

Kết quả:

```text
.toolkit/                  # manifest và hướng dẫn tích hợp
.spec-product/             # spec-driven-product-toolkit
.logic/                    # Logic Toolkit persistent behavior memory
.steward/                  # ops-toolkit
```

Script không tự cài package ngoài, không ghi đè state đã có, và trả exit code khác 0 khi thiếu component hoặc phát hiện xung đột.

## Quét logic để tái sử dụng

```powershell
python logic-toolkit\scripts\scan_logic.py `
  --project D:\path\to\your\app `
  --write-report
```

Scanner chỉ đề xuất candidate. Pattern chỉ được đưa vào `library/` sau khi đã loại bỏ chi tiết project-specific và kiểm tra portability.
