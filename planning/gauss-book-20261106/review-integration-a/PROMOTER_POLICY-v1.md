# Guarded local promoter policy — PASS, not executed

Reviewed exact promote_v1.py a8e206fd, including its sole delta from c79455c8: the required root/native-visual-v1 gate. This review did not import or execute the promoter.

All named acceptance/build/native/visual/browser records must exist and pass before any write. Source integration targets, current native scientific sources, old live book assets, focused/note source records, exact source and destination pinsets, all pending-name absences, source HEAD and index are checked before creating the promotion output directory. The independent artifact gate must supply both exact18-source hashes and exact18-target-before hashes (null for new targets). Its absence or mismatch stops before writes.

The destination set is bounded: three book PDF/log/toc files, eight focused/note PDF/log files and exactly seven native changes. The seven allowed native paths are main.html; the three gauss-tail shared source/figure-wrapper files; and the three original gauss-tail figure tex/pdf/svg assets. The current frozen native tree produces precisely those seven differences. No inherited CSS, Javascript, lab, old figure or unrelated production path is allowed. Current source paths correctly reuse concise run-v2 and detailed/book run-v3 artifacts.

For the current records the independently inspected edition counts are333 book pages,10299 MathML with9810 old literal subtrees,389 tables,14 labs,31 SVG references and40 chapters; focused81/228 and notes39/118. These are artifact-record/source-contract observations, not a new PDF/browser verification by this reviewer.

Each existing destination is copied to a newly created promotion backup before overwrite. Source bytes are copied through a uniquely named, previously absent pending file, compared byte-for-byte, then replaced atomically per file. main.html is sorted last. This is per-file atomic replacement with preserved recovery bytes, not a claim of an all18-file rollback transaction. The final receipt pins the gates and independent maps, verifies the index and final HTML and discloses local-only/no public release/no completion claims. No Git/index/ref/auth/network operation writes occur in this producer.

The native palette amendment is limited to the new gauss-tail image tag (filter:none!important, white canvas). Its actual SVG/PDF/TeX bytes equal the original figure source assets. The root visual gate pins the current native record and final browser receipt. No new visual approval or old error-filter review is implied here.

Policy accepted for these exact producer bytes and frozen input contracts. The pending C artifact acceptance remains an execution precondition; this policy receipt does not supply it. No promoter, build, browser, scientific-data check, source/index edit or publication operation was executed.
