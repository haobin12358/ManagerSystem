
<template>
  <div>
    <div class="page-total">
      总记录数：{{total}} 个
    </div>
    <div class="page-current">
      当前：第 {{page}} 页
    </div>
    <div class="page-pages">
      共 {{pages}} 页
    </div>
    <div class="page-button">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="1000">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import user from '../../common/json/userInfo'
  export default {
    name: 'Pagination',
    created:function() {
      this.sendData()
      this.setOptions()
    },
    data () {
      return {
        options: [],
        value: '',
        user: user.slice(0, 10),
        total: user.length,
        page: 1,
        pages: Math.ceil(user.length/10),
      }
    },
    methods:{
      sendData: function () {
        this.$emit('partUser', this.user)
      },
      firstPage() {
        this.page = 1
        this.user = user.slice(0, 10)
        this.sendData()
      },
      lastPage() {
        if(this.page < 2){
          console.log(this.page)
        }else {
          this.page = this.page-1
          this.user = user.slice(this.page*10-10, this.page*10)
          this.sendData()
        }
      },
      nextPage() {
        if(this.page > this.pages-1) {
          console.log(this.page)
        }else {
          this.page = this.page+1
          this.user = user.slice(this.page*10-10, this.page*10)
          this.sendData()
        }
      },
      endPage() {
        this.page = this.pages
        this.user = user.slice(this.pages*10-10, this.pages*10)
        this.sendData()
      },
      change() {
        this.page = this.value
        this.user = user.slice(this.value*10-10, this.value*10)
        this.sendData()
      },
      setOptions() {
        for(var i=0;i<this.pages;i++) {
          this.options.push({
            value: i+1,
            label: '第 '+(i+1)+' 页'
          })
        }
      }
    }
  }
</script>

<style scoped>
  .page-total {
    float: left;
    width: 115px;
    font-size: 14px;
    margin: 0 0 55px 30px;
  }
  .page-current {
    float: left;
    width: 115px;
    font-size: 14px;
    margin: 0 0 55px 30px;
  }
  .page-pages {
    float: left;
    width: 115px;
    font-size: 14px;
    margin: 0 0 55px 0;
  }
  .page-button {
    width: 400px;
    float: right;
    margin-top: -10px;
  }
  .firstPage {
    color: #000000;
  }
  .lastPage {
    color: #000000;
  }
  .nextPage {
    color: #000000;
  }
  .endPage {
    color: #000000;
  }
  .page-select {
    margin: 0 5px 0 5px;
    width: 93px;
  }
</style>
