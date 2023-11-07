{{/*
Expand the name of the chart.
*/}}
{{- define "libchart.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}


{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "libchart.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}


{{/*
Common labels
*/}}
{{- define "libchart.labels" -}}
helm.sh/chart: {{ include "libchart.chart" . }}
{{ include "libchart.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "libchart.selectorLabels" -}}
app.kubernetes.io/name: {{ include "libchart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}