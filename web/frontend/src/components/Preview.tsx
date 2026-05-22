interface PreviewProps {
  content: string
}

export default function Preview({ content }: PreviewProps) {
  const handleDownload = () => {
    if (!content) return
    
    const element = document.createElement('a')
    const file = new Blob([content], { type: 'text/markdown' })
    element.href = URL.createObjectURL(file)
    element.download = `memo-${new Date().toISOString().split('T')[0]}.md`
    document.body.appendChild(element)
    element.click()
    document.body.removeChild(element)
  }

  return (
    <div className="space-y-4 h-full">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-serif font-semibold text-light-900">
          プレビュー
        </h2>
        {content && (
          <button
            onClick={handleDownload}
            className="btn-secondary text-sm"
          >
            ⬇️ ダウンロード
          </button>
        )}
      </div>

      {content ? (
        <div className="card p-6 h-96 overflow-y-auto prose prose-sm max-w-none">
          <pre className="bg-light-50 p-4 rounded-lg overflow-x-auto text-xs font-mono text-light-700 whitespace-pre-wrap break-words">
            {content}
          </pre>
        </div>
      ) : (
        <div className="card p-6 h-96 flex items-center justify-center text-light-400">
          <p className="text-center">
            メモを入力して、「メモを整理」ボタンを
            <br />
            クリックすると、ここにプレビューが表示されます
          </p>
        </div>
      )}
    </div>
  )
}
