# KyoProTraining

競技プログラムのスクリプト置き場

# よく使うライブラリ

### 入力受付

```python
s = input()
n = int(input())
a,b = map(int,input().split())
nums = list(map(int, input().split()))
```

### GitCommand

ステップ1：フォルダに移動

```bash
cd KyoProTraining
```

ステップ2：最新状態を取得

```bash
git pull origin main
```

ステップ3：ディレクトリとファイルを作る

```bash
mkdir ABC001          # フォルダ作成（番号は合わせてね）
cp main.py ABC001/A.py  # main.pyをA.pyとしてコピー
```

ステップ4：変更をステージング

```bash
git add ABC001/A.py
```

ステップ5：コミット

```bash
git commit -m "ABC001 A問題AC"
```

ステップ6：GitHubに反映

```bash
git push origin main
```
