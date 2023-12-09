const MOSCOW_TIME_OFFSET = 3

export function getMoscowTime(): [string, string] {
  const currentTimestamp = Date.now()
  const date = new Date(currentTimestamp)
  const utcHours = date.getUTCHours()
  date.setHours(utcHours + MOSCOW_TIME_OFFSET)

  return date.toLocaleString('ru').replace(/,/g, '').split(' ') as [string, string]
}
