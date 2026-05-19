export type TextLength = 'short' | 'medium' | 'long'
export type TextStyle = 'formal' | 'casual' | 'humorous' | 'academic'
export type PolishIntensity = 'light' | 'medium' | 'strong'
export type RewriteStyle = 'concise' | 'detailed' | 'professional'
export type SummaryFormat = 'paragraph' | 'bullet'
export type TargetModel = 'text' | 'image' | 'video' | 'audio'

export interface TextGenerateRequest {
  prompt: string
  length: TextLength
  style: TextStyle
}

export interface TextGenerateResponse {
  success: boolean
  data: {
    content: string
    word_count: number
  }
  response_time_ms: number
}

export interface TextPolishRequest {
  text: string
  intensity: PolishIntensity
}

export interface TextPolishResponse {
  success: boolean
  data: {
    original: string
    polished: string
    word_count: number
  }
  response_time_ms: number
}

export interface TextRewriteRequest {
  text: string
  style: RewriteStyle
}

export interface TextRewriteResponse {
  success: boolean
  data: {
    original: string
    rewritten: string
    similarity_score: number
    word_count: number
  }
  response_time_ms: number
}

export interface TextSummarizeRequest {
  text: string
  ratio: number
  format: SummaryFormat
}

export interface TextSummarizeResponse {
  success: boolean
  data: {
    original_length: number
    summary_length: number
    summary: string
    key_points: string[]
  }
  response_time_ms: number
}

export interface TextOptimizeRequest {
  prompt: string
  target_model: TargetModel
}

export interface TextOptimizeResponse {
  success: boolean
  data: {
    original: string
    optimized: string
    improvements: string[]
  }
  response_time_ms: number
}

export interface ErrorResponse {
  success: boolean
  error_code: string
  error_message: string
}

export type ImageStyle = 'realistic' | 'cartoon' | 'abstract' | 'anime' | 'photographic'
export type ImageSize = '512x512' | '1024x1024' | '1024x1792'

export interface ImageGenerateRequest {
  prompt: string
  style?: ImageStyle
  size?: ImageSize
  num_images?: number
}

export interface ImageGenerateResponse {
  success: boolean
  data: {
    images: string[]
    prompt: string
    style: string
    size: string
  }
  response_time_ms: number
}