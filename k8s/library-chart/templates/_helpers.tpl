{{- define "library-chart.labels" -}}
  labels:
    app.kubernetes.io/name: {{ include "library-chart.name" . }}
    app.kubernetes.io/instance: {{ .Release.Name }}
    app.kubernetes.io/version: {{ include "library-chart.version" . }}
    app.kubernetes.io/managed-by: {{ .Release.Service | quote }}
{{- end -}}
