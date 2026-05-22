interface EditorProps {
  content: string
  onChange: (content: string) => void
  memoType: string | null
  onMemoTypeChange: (type: 'meeting' | 'learning' | 'interview' | 'idea' | null) => void
  onProcess: () => void
  isProcessing: boolean
}

const memoTypes = [
  { value: 'meeting', label: '📋 会議', color: 'blue' },
  { value: 'learning', label: '📚 学習', color: 'green' },
  { value: 'interview', label: '🎤 ヒアリング', color: 'purple' },
  { value: 'idea', label: '💡 アイデア', color: 'orange' },
]

export default function Editor({
  content,
  onChange,
  memoType,
  onMemoTypeChange,
  onProcess,
  isProcessing,
}: EditorProps) {
  return (
    <div className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-light-700 mb-3">
          メモの種類（任意）
        </label>
        <div className="grid grid-cols-2 gap-2">
          <button
            onClick={() => onMemoTypeChange(null)}
            className={`py-2 px-3 rounded-lg font-medium transition-all ${
              memoType === null
                ? 'bg-light-900 text-white'
                : 'bg-light-100 text-light-700 hover:bg-light-200'
            }`}
          >
            自動判定
          </button>
          {memoTypes.map((type) => (
            <button
              key={type.value}
              onClick={() => onMemoTypeChange(type.value as any)}
              className={`py-2 px-3 rounded-lg font-medium transition-all ${
                memoType === type.value
                  ? 'bg-light-900 text-white'
                  : 'bg-light-100 text-light-700 hover:bg-light-200'
              }`}
            >
              {type.label}
            </button>
          ))}
        </div>
      </div>

      <div>
        <label htmlFor="memo" className="block text-sm font-medium text-light-700 mb-2">
          メモを入力
        </label>
        <textarea
          id="memo"
          value={content}
          onChange={(e) => onChange(e.target.value)}
          placeholder="ここにメモを入力してください。思いついたことをそのまま書いてOK。"
          className="input-base h-96 resize-none"
        />
      </div>

      <button
        onClick={onProcess}
        disabled={isProcessing}
        className={`w-full btn-primary disabled:opacity-50 disabled:cursor-not-allowed ${
          isProcessing ? 'opacity-50' : ''
        }`}
      >
        {isProcessing ? '処理中...' : '✨ メモを整理'}
      </button>
    </div>
  )
}
