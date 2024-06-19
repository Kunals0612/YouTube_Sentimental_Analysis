import Image from "next/image";
import { NextUIProvider} from "@nextui-org/react";
import LinkInput from "./LinkInput";
export default function Home() {
  return (
  
      <main className="h-[100vh]">   
        <NextUIProvider>
          <main className="dark text-foreground bg-background mainClass">
            <LinkInput/>
          </main>
        </NextUIProvider>
      </main>
  );
}
