import os
import json

# -------------------------
# CREATE FOLDER STRUCTURE
# -------------------------

folders = [
    "content/master-documents",
    "content/modules/CS",
    "content/projects",
    "content/curriculum",
    "schemas",
    "kernel"
]

for f in folders:
    os.makedirs(f, exist_ok=True)

# -------------------------
# CREATE DM-00
# -------------------------

dm00 = """---
id: DM-00
title: HKI Bootstrap
type: master-document
status: active
version: 1.0.0
---

# HKI Bootstrap System

Single Source of Truth: YAML frontmatter
"""

with open("content/master-documents/DM-00.md", "w") as f:
    f.write(dm00)

# -------------------------
# CREATE DM-01
# -------------------------

dm01 = """---
id: DM-01
title: HKI Kernel System
type: master-document
dependencies: [DM-00]
---

# Kernel System

Generated automatically via CI/CD.
"""

with open("content/master-documents/DM-01.md", "w") as f:
    f.write(dm01)

# -------------------------
# CREATE INITIAL MODULE
# -------------------------

mod = """---
id: MOD-CS-001
title: Introduction to Systems
type: module
dependencies: []
---

# Intro to Systems
"""

with open("content/modules/CS/MOD-CS-001.md", "w") as f:
    f.write(mod)

# -------------------------
# CREATE KERNEL PLACEHOLDERS
# -------------------------

kernel = {
    "master_registry": {},
    "dependency_graph": {},
    "competency_graph": {}
}

with open("kernel/master_registry.json", "w") as f:
    json.dump(kernel["master_registry"], f, indent=2)

with open("kernel/dependency_graph.json", "w") as f:
    json.dump(kernel["dependency_graph"], f, indent=2)

with open("kernel/competency_graph.json", "w") as f:
    json.dump(kernel["competency_graph"], f, indent=2)

print("HKI Bootstrap Complete")
