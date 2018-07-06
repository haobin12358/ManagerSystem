<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script type="text/ecmascript-6">
export default {
  name: 'App'
}
</script>

<style lang="less" rel="stylesheet/less" scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  min-height: 100%;
  /*margin-top: 60px;*/
}
</style>
