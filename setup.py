#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Memo Structurizer
Creates necessary directory structure and initializes configuration
"""

import os
import sys
from pathlib import Path
import json


def setup():
    """Run setup for memo-structurizer."""
    print("=" * 60)
    print("🗂️  Memo Structurizer セットアップ")
    print("=" * 60)
    
    # Get home directory
    home = str(Path.home())
    base_dir = os.path.join(home, "Documents", "my-knowledge")
    
    # Create base directory
    print(f"\n📁 ディレクトリを作成中: {base_dir}")
    try:
        os.makedirs(base_dir, exist_ok=True)
        print(f"✓ ディレクトリ作成完了")
    except Exception as e:
        print(f"❌ エラー: {e}")
        return False
    
    # Create .gitignore in base directory
    gitignore_path = os.path.join(base_dir, ".gitignore")
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, "w", encoding="utf-8") as f:
            f.write("# Ignore all memo files\n*.md\n.DS_Store\n")
        print(f"✓ .gitignore を作成")
    
    # Create config file
    config_path = os.path.join(base_dir, "config.json")
    if not os.path.exists(config_path):
        config = {
            "base_directory": base_dir,
            "version": "1.0",
            "created_at": "2026-05-22",
            "memo_types": ["meeting", "learning", "interview", "idea"]
        }
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        print(f"✓ 設定ファイルを作成: config.json")
    
    # Create sample directory for today
    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")
    today_dir = os.path.join(base_dir, today)
    
    print(f"\n📅 本日のディレクトリを作成中: {today_dir}")
    try:
        os.makedirs(today_dir, exist_ok=True)
        print(f"✓ ディレクトリ作成完了")
    except Exception as e:
        print(f"❌ エラー: {e}")
        return False
    
    # Create a sample memo file
    sample_file = os.path.join(today_dir, "00-README.md")
    if not os.path.exists(sample_file):
        with open(sample_file, "w", encoding="utf-8") as f:
            f.write("""# Memo Structurizer - 本日のメモ保存場所

このフォルダに、本日整理されたメモが保存されます。

## 使い方

```bash
# 会議メモを整理
python memo_structurizer.py "会議" "メモの内容..."

# 学習メモを整理
python memo_structurizer.py "学習" "メモの内容..."

# ヒアリングメモを整理
python memo_structurizer.py "ヒアリング" "メモの内容..."

# アイデアメモを整理
python memo_structurizer.py "アイデア" "メモの内容..."
```

## メモ種類が不明な場合

メモ種類を指定しないと、自動判定またはユーザーに質問します：

```bash
python memo_structurizer.py "メモの内容..."
```

詳細は README.md を参照してください。
""")
        print(f"✓ サンプルファイルを作成: 00-README.md")
    
    # Print summary
    print("\n" + "=" * 60)
    print("✅ セットアップ完了！")
    print("=" * 60)
    print(f"\n📂 保存ディレクトリ: {base_dir}")
    print(f"📅 本日のフォルダ: {today_dir}")
    print("\n次のコマンドでメモを整理できます：")
    print('  python memo_structurizer.py "会議" "メモの内容..."')
    print("\n詳細は README.md を参照してください。")
    
    return True


if __name__ == "__main__":
    try:
        success = setup()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ セットアップ中にエラーが発生しました: {e}")
        sys.exit(1)
