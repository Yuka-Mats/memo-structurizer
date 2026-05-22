#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Memo Structurizer
Automatically structure scattered text notes into organized Markdown files.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import json


class MemoStructurizer:
    """Main class for structuring messy notes into organized markdown files."""
    
    # Supported memo types
    MEMO_TYPES = {
        "会議": "meeting",
        "学習": "learning",
        "ヒアリング": "interview",
        "アイデア": "idea"
    }
    
    def __init__(self, base_dir: Optional[str] = None):
        """Initialize the structurizer with a base directory."""
        if base_dir is None:
            # Default to ~/Documents/my-knowledge
            home = str(Path.home())
            base_dir = os.path.join(home, "Documents", "my-knowledge")
        
        self.base_dir = base_dir
        self.today = datetime.now().strftime("%Y-%m-%d")
        self.output_dir = os.path.join(base_dir, self.today)
        
        # Ensure output directory exists
        self._ensure_directory()
    
    def _ensure_directory(self) -> None:
        """Create output directory if it doesn't exist."""
        os.makedirs(self.output_dir, exist_ok=True)
        print(f"✓ Output directory ready: {self.output_dir}")
    
    def determine_memo_type(self, memo_content: str) -> Optional[str]:
        """
        Determine memo type from content.
        Returns 'meeting', 'learning', 'interview', or 'idea'.
        Returns None if type cannot be determined.
        """
        content_lower = memo_content.lower()
        
        # Keywords for each type
        meeting_keywords = ["会議", "meeting", "ミーティング", "会議", "議論", "決定", "アクション", "参加者"]
        learning_keywords = ["学習", "learning", "学ぶ", "勉強", "概念", "理解", "参考資料", "知識"]
        interview_keywords = ["ヒアリング", "interview", "インタビュー", "質問", "回答", "発見", "聞き取り"]
        idea_keywords = ["アイデア", "idea", "ブレイン", "提案", "検討", "実装", "機能"]
        
        # Check for keyword matches
        if any(kw in content_lower for kw in meeting_keywords):
            return "meeting"
        elif any(kw in content_lower for kw in learning_keywords):
            return "learning"
        elif any(kw in content_lower for kw in interview_keywords):
            return "interview"
        elif any(kw in content_lower for kw in idea_keywords):
            return "idea"
        
        return None
    
    def ask_memo_type(self) -> str:
        """Ask user to specify memo type."""
        print("\n❓ メモの種類が分かりません。")
        print("以下から選んでください：")
        print("  1. 会議")
        print("  2. 学習")
        print("  3. ヒアリング")
        print("  4. アイデア")
        
        while True:
            choice = input("\n選択 (1-4): ").strip()
            type_map = {"1": "meeting", "2": "learning", "3": "interview", "4": "idea"}
            if choice in type_map:
                return type_map[choice]
            print("❌ 1-4 の数字で選んでください")
    
    def structure_meeting(self, content: str, title: str = "Meeting") -> Dict[str, str]:
        """Structure meeting notes."""
        files = {}
        
        # Overview file
        overview = f"""# 会議: {title}

**日付**: {self.today}
**作成者**: 

## アジェンダ
- 

## 議論
### トピック 1
- 

## 決定
- 

## アクション アイテム
- [ ] アクション 1 - 担当者: 
- [ ] アクション 2 - 担当者: 

## フォローアップ
- 

---

## 元のメモ
{content}
"""
        files["01-会議-概要.md"] = overview
        
        return files
    
    def structure_learning(self, content: str, title: str = "Learning") -> Dict[str, str]:
        """Structure learning notes."""
        files = {}
        
        overview = f"""# 学習: {title}

**日付**: {self.today}
**ソース**: 

## 主要概念
- 概念 1: 定義と説明
- 概念 2: 定義と説明

## 主な学び
1. 学び 1
2. 学び 2

## 詳細
### トピック 1
詳細な説明...

### トピック 2
詳細な説明...

## 質問・確認が必要な点
- 質問 1
- 質問 2

## 参考資料
- リンク/ソース 1
- リンク/ソース 2

---

## 元のメモ
{content}
"""
        files["01-学習-概要.md"] = overview
        
        return files
    
    def structure_interview(self, content: str, title: str = "Interview") -> Dict[str, str]:
        """Structure interview notes."""
        files = {}
        
        overview = f"""# ヒアリング: {title}

**日付**: {self.today}
**インタビュアー**: 
**インタビュイー**: 

## 主要な発見
- 発見 1
- 発見 2

## 詳細なインサイト
### トピック 1
Q: 質問内容
A: 回答/レスポンス

### トピック 2
Q: 質問内容
A: 回答/レスポンス

## アクション アイテム / 次のステップ
- [ ] アイテム 1
- [ ] アイテム 2

## フォローアップ質問
- 質問 1
- 質問 2

---

## 元のメモ
{content}
"""
        files["01-ヒアリング-概要.md"] = overview
        
        return files
    
    def structure_idea(self, content: str, title: str = "Ideas") -> Dict[str, str]:
        """Structure idea notes."""
        files = {}
        
        overview = f"""# アイデア: {title}

**日付**: {self.today}
**背景/解決する問題**: 

## コアアイデア
### アイデア 1: タイトル
- 説明
- なぜうまくいくのか
- 見込まれる利点
- 課題

### アイデア 2: タイトル
- 説明
- なぜうまくいくのか
- 見込まれる利点
- 課題

## 実装時の検討事項
- 検討事項 1
- 検討事項 2

## 必要なリソース
- リソース 1
- リソース 2

## 関連アイデア / バリエーション
- バリエーション 1
- バリエーション 2

---

## 元のメモ
{content}
"""
        files["01-アイデア-概要.md"] = overview
        
        return files
    
    def save_files(self, files: Dict[str, str]) -> List[str]:
        """Save structured files to disk."""
        saved_files = []
        
        for filename, content in files.items():
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            saved_files.append(filepath)
            print(f"✓ 保存: {filename}")
        
        return saved_files
    
    def process_memo(self, memo_content: str, memo_type: Optional[str] = None, title: str = "メモ") -> List[str]:
        """
        Process a memo and structure it into files.
        
        Args:
            memo_content: The raw memo text
            memo_type: Type of memo ('meeting', 'learning', 'interview', 'idea')
            title: Title for the memo
        
        Returns:
            List of created file paths
        """
        # Determine memo type if not provided
        if memo_type is None:
            detected_type = self.determine_memo_type(memo_content)
            if detected_type is None:
                memo_type = self.ask_memo_type()
            else:
                memo_type = detected_type
        
        print(f"\n📝 メモ種類: {memo_type}")
        
        # Structure based on type
        if memo_type == "meeting":
            files = self.structure_meeting(memo_content, title)
        elif memo_type == "learning":
            files = self.structure_learning(memo_content, title)
        elif memo_type == "interview":
            files = self.structure_interview(memo_content, title)
        elif memo_type == "idea":
            files = self.structure_idea(memo_content, title)
        else:
            raise ValueError(f"Unknown memo type: {memo_type}")
        
        # Save files
        print(f"\n💾 ファイルを保存中...\n")
        saved_files = self.save_files(files)
        
        print(f"\n✅ 完了！")
        print(f"📂 保存先: {self.output_dir}")
        print(f"📄 作成されたファイル: {len(saved_files)} 個")
        
        return saved_files


def main():
    """Main entry point for CLI usage."""
    if len(sys.argv) < 2:
        print("使い方:")
        print("  python memo_structurizer.py '会議／学習／ヒアリング／アイデア' 'メモの内容'")
        print("\n例:")
        print("  python memo_structurizer.py '会議' '今日の会議で決まったことはXXX...'")
        sys.exit(1)
    
    memo_type = sys.argv[1] if len(sys.argv) > 1 else None
    memo_content = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else input("メモの内容を入力してください:\n")
    
    # Map Japanese type names to English
    type_map = {
        "会議": "meeting",
        "学習": "learning",
        "ヒアリング": "interview",
        "アイデア": "idea"
    }
    
    if memo_type in type_map:
        memo_type = type_map[memo_type]
    elif memo_type and memo_type not in type_map.values():
        memo_type = None
    
    structurizer = MemoStructurizer()
    structurizer.process_memo(memo_content, memo_type)


if __name__ == "__main__":
    main()
