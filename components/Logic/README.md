# Logic Toolkit

`logic-toolkit` là bộ cài đặt tích hợp ba toolkit độc lập:

1. `spec-driven-product-toolkit` — sản phẩm cần xây gì và workflow delivery.
2. `logic-toolkit` — phân tích tính đầy đủ và nhất quán của logic hành vi sản phẩm: state, transition, điều kiện, effect, invariant, lỗi và các bề mặt phụ thuộc.
3. `ops-toolkit` — repository/product có maintainable, attributable và handoff-ready không.

`.logic/` lưu các quyết định hành vi đã xác nhận để những lần phát triển tiếp theo không làm mất ngữ cảnh; đây là cơ chế hỗ trợ, không phải mục tiêu chính hay general-purpose agent memory. Toolkit cũng có **reusable logic library** để tích lũy các invariant, state pattern và behavior pattern có bằng chứng, có thể dùng qua nhiều dự án.

Bộ cài đặt này là integration layer, không hợp nhất nội dung hoặc tạo checklist trùng lặp. Mỗi toolkit giữ ownership và thư mục state riêng. Điều phối multi-agent thuộc tool riêng, không thuộc Logic Toolkit.

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
.logic/                    # project-specific product behavior records
.steward/                  # ops-toolkit
```

Script không tự cài package ngoài, không ghi đè state đã có, và trả exit code khác 0 khi thiếu component hoặc phát hiện xung đột.

## Quét logic để tái sử dụng

```powershell
python logic-toolkit\scripts\scan_logic.py `
  --project D:\path\to\your\app `
  --write-report
```

Scanner chỉ tìm các dòng có dấu hiệu để review; nó không phân tích hay xác nhận logic. Pattern chỉ được đưa vào `library/` sau khi đã khái quát khỏi chi tiết project-specific, có cách kiểm chứng và được review portability.

## Ranh giới Logic

- **Spec Driven:** sản phẩm cần xây gì, phạm vi/requirement là gì, tiêu chí chấp nhận và delivery gate.
- **Logic:** behavior có đầy đủ và nhất quán không — actor, điều kiện, state/transition, effect, invariant, lỗi/retry/recovery, và ảnh hưởng lên UI/API/dữ liệu/quyền truy cập.
- **Ops:** repository có thể duy trì, truy xuất nguồn gốc và bàn giao được không.
- **Multi-agent tool riêng:** phân công, delegation, phối hợp và trạng thái giữa các agent.

Tham khảo [source evaluation](../../docs/logic-source-evaluation.md): nguồn trọng tâm của Logic là state modeling và kiểm thử invariant/stateful; repo về agent memory, task graph hoặc orchestration không phải nền tảng chủ đề.
