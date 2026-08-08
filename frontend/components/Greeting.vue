<script setup>
// Intentionally smelly Vue SFC for HeyEddi triage + review scoring.
const props = defineProps({ html: { type: String, required: true } })
</script>

<template>
  <!-- v-html with unsanitized prop — XSS vector -->
  <div class="greeting" v-html="html" />
</template>
