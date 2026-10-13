import { checkHeaders, checkNumstat } from "./pc.mjs";
const cases = {
 ok:"diff --git a/a b/a\nindex 1111111..2222222 100644\n--- a/a\n+++ b/a\n@@ -1 +1 @@\n-a\n+b\n",
 modeonly:"diff --git a/a b/a\nold mode 100644\nnew mode 100755\n",
 idx755:"diff --git a/a b/a\nindex 1111111..2222222 100755\n--- a/a\n+++ b/a\n@@ -1 +1 @@\n-a\n+b\n",
 symlink:"diff --git a/a b/a\ndeleted file mode 100644\n",
 typechange:"diff --git a/a b/a\nnew file mode 120000\n",
 rename:"diff --git a/a b/b\nsimilarity index 100%\nrename from a\nrename to b\n",
 binary:"diff --git a/a b/a\nindex 1..2\nBinary files a/a and b/a differ\n",
 crlf_mode:"diff --git a/a b/a\r\nold mode 100644\r\nnew mode 120000\r\n",
 indented:"diff --git a/a b/a\n old mode 100644\n",
};
for (const [k,v] of Object.entries(cases)) console.log(k, JSON.stringify(checkHeaders(v)));
