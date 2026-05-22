import { useState } from 'react'
import Editor from './components/Editor'
import Preview from './components/Preview'
import Header from './components/Header'

function App() {
  const [memoContent, setMemoContent] = useState('')
  const [memoType, setMemoType] = useState<'meeting' | 'learning' | 'interview' | 'idea' | null>(null)
  const [isProcessing, setIsProcessing] = useState(false)
  const [structuredMemo, setStructuredMemo] = useState('')

  const handleProcess = async () => {
    if (!memoContent.trim()) {
      alert('メモを入力してください')
      return
    }

    setIsProcessing(true)
    try {
      const response = await fetch('/api/structure', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          content: memoContent,
          memo_type: memoType,
        }),
      })

      if (!response.ok) {
        throw new Error('処理に失敗しました')
      }

      const data = await response.json()
      setStructuredMemo(data.structured_content)
      setMemoType(data.memo_type)
    } catch (error) {
      console.error('Error:', error)
      alert('処理中にエラーが発生しました')
    } finally {
      setIsProcessing(false)
    }
  }

  return (
    <div className="min-h-screen bg-light-50">
      <Header />
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div>
            <Editor
              content={memoContent}
              onChange={setMemoContent}
              memoType={memoType}
              onMemoTypeChange={setMemoType}
              onProcess={handleProcess}
              isProcessing={isProcessing}
            />
          </div>
          <div>
            <Preview content={structuredMemo} />
          </div>
        </div>
      </main>
    </div>
  )
}

export default App
