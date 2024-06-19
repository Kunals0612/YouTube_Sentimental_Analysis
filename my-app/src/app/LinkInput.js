import React from 'react'
import { Input } from "@nextui-org/react";
import { Button } from "@nextui-org/react";
export default function LinkInput() {
  return (
    <>
          <h1 className='absolute top-[10%] left-[40%] text-2xl text-gray-400'>Enter YouTube Video Link</h1>
    <div className="flex w-[800px] absolute top-[20%] left-[23%] flex-wrap md:flex-nowrap gap-4">
          <Input type="text" variant="faded" label="Link" placeholder='Enter the link' />
          <Button className="relative top-1" color="primary" size='lg'>
              Submit
          </Button>
    </div>
    </>
    
  )
}
