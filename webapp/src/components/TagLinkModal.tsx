import React from 'react';
import { Modal, Box, Typography, Button } from '@mui/material';

const style = {
  position: 'absolute' as 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  p: 4,
  borderRadius: 4,
};

interface ITagLinkModal {
  open: boolean;
  handleTagLink: (answer: string) => void;
}

const TagLinkModal = (props: ITagLinkModal) => {
  const { open, handleTagLink } = props;

  return (
    <div>
      <Modal open={open}>
        <Box sx={style}>
          <Typography
            sx={{
              textAlign: 'center',
            }}
            variant="h6"
          >
            ¿Es una colección de algoritmos para la toma de decisiones
            automatizadas?
          </Typography>
          <div
            style={{
              marginTop: '30px',
              textAlign: 'center',
            }}
          >
            <Button
              sx={{ backgroundColor: '#60D660', color: 'black' }}
              onClick={() => handleTagLink('yes')}
            >
              Yes
            </Button>
            <Button
              sx={{
                marginLeft: '20px',
                backgroundColor: '#D66460',
                color: 'black',
              }}
              onClick={() => handleTagLink('no')}
            >
              No
            </Button>
            <Button
              sx={{
                marginLeft: '20px',
                backgroundColor: '#F0E666',
                color: 'black',
              }}
              onClick={() => handleTagLink('maybe')}
            >
              Maybe
            </Button>
          </div>
          <div style={{ textAlign: 'center', marginTop: '20px' }}>
            <Button
              sx={{
                marginLeft: '20px',
                backgroundColor: '#ff781f',
                color: 'black',
              }}
              onClick={() => handleTagLink('academic')}
            >
              Academic
            </Button>
          </div>
          {/* <div style={{ textAlign: 'center', marginTop: '20px' }}>
            <Button
              sx={{
                marginLeft: '20px',
                backgroundColor: '#ff781f',
                color: 'black',
              }}
              onClick={() => handleTagLink(null)}
            >
              Academic
            </Button>
          </div> */}
        </Box>
      </Modal>
    </div>
  );
};

export default TagLinkModal;
