{{/*
Expand the name of the chart.
*/}}
{{- define "helm-python-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "helm-python-app.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "helm-python-app.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "helm-python-app.labels" -}}
helm.sh/chart: {{ include "helm-python-app.chart" . }}
{{ include "helm-python-app.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "helm-python-app.selectorLabels" -}}
app.kubernetes.io/name: {{ include "helm-python-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "helm-python-app.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "helm-python-app.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}

{{/*
Define secret envs
*/}}
{{- define "helm-python-app.envsecrets" -}}
{{- if .Values.mysecret.name1 }}
- name: "my-secret"
  valueFrom:
    secretKeyRef:
      name: {{ .Values.mysecret.name1 }}
      key: {{ .Values.mysecret.key1 }}
- name: "my-secret-two"
  valueFrom:
    secretKeyRef:
      name: {{ .Values.mysecret.name2 }}
      key: {{ .Values.mysecret.key2 }}
{{- else }}
- name: "password"
  value: ""
{{- end }}
{{- end }}
